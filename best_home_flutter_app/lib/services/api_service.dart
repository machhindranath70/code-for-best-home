import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://127.0.0.1:8000/api'; // Replace with your IP if needed

  static Future<bool> submitRegistration(Map<String, dynamic> data) async {
    final url = Uri.parse('$baseUrl/register/');

    try {
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode(data),
      );

      return response.statusCode == 201;
    } catch (e) {
      print('❌ Error submitting registration: $e');
      return false;
    }
  }

  static Future<List<dynamic>> fetchRegistrations() async {
    final url = Uri.parse('$baseUrl/registrations/'); // You need to implement this in Django

    try {
      final response = await http.get(url);
      if (response.statusCode == 200) {
        return jsonDecode(response.body);
      }
    } catch (e) {
      print('❌ Error fetching registrations: $e');
    }
    return [];
  }
}
