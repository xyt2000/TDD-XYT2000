[1mdiff --git a/functional_tests.py b/functional_tests.py[m
[1mindex b8ca631..2745603 100644[m
[1m--- a/functional_tests.py[m
[1m+++ b/functional_tests.py[m
[36m@@ -29,13 +29,15 @@[m [mclass NewVisitorTest(unittest.TestCase):#(1)[m
 		#when she hits enter,the page updates,and now the page lists[m
 		#"1":Buy peocock feathers" as an item in a to-do list[m
 		inputbox.send_keys(Keys.ENTER)[m
[31m-		time.sleep(10)[m
[32m+[m		[32mtime.sleep(1)[m
 		table = self.browser.find_element_by_id('id_list_table')[m
 		rows = table.find_elements_by_tag_name('tr')[m
[31m-		self.assertTrue([m
[31m-			any(row.text == '1:Buy peacock feathers' for row in rows),[m
[31m-			"New to-do item did not appear in table"[m
[31m-		)[m
[32m+[m		[32m#self.assertTrue([m
[32m+[m		[32m#	any(row.text == '1:Buy peacock feathers' for row in rows),[m
[32m+[m		[32m#	f"New to-do item did not appear in table. Contents were:\n{table.text}"[m
[32m+[m		[32m#)[m
[32m+[m		[32mself.assertIn('1:Buy peacock feathers',[row.text for row in rows])[m
[32m+[m		[32mself.assertIn('2:Use peacock feathers to make a fly',[row.text for row in rows])[m
 		#There is still a text box inviting her to add another item.She[m
 		#enters "use peocock feathers to make a fly"(Edith is very methodical)[m
 		self.fail('finish the test')[m
[1mdiff --git a/lists/templates/home.html b/lists/templates/home.html[m
[1mindex d85e165..e6961ea 100644[m
[1m--- a/lists/templates/home.html[m
[1m+++ b/lists/templates/home.html[m
[36m@@ -5,7 +5,11 @@[m
 	<body>[m
 		<h1>Your To-Do list</h1>[m
 		<form method="POST">[m
[31m-		<input name="item_text" id="id_new_item" placeholder="Enter a to-do item"/></form>[m
[31m-		<table id="id_list_table"></table>[m
[32m+[m		[32m<input name="item_text" id="id_new_item" placeholder="Enter a to-do item"/>[m
[32m+[m		[32m{% csrf_token %}[m
[32m+[m		[32m</form>[m
[32m+[m		[32m<table id="id_list_table">[m
[32m+[m			[32m<tr><td>1:{{ new_item_text }}</td></tr>[m
[32m+[m		[32m</table>[m
 	</body>[m
 </html>[m
\ No newline at end of file[m
[1mdiff --git a/lists/tests.py b/lists/tests.py[m
[1mindex befd8a7..8f0cad6 100644[m
[1m--- a/lists/tests.py[m
[1m+++ b/lists/tests.py[m
[36m@@ -6,4 +6,8 @@[m [mclass HomePageTest(TestCase):[m
 # Create your tests here.[m
 	def test_home_page_returns_correct_html(self):[m
 		response = self.client.get('/')[m
[32m+[m		[32mself.assertTemplateUsed(response,'home.html')[m
[32m+[m	[32mdef test_can_save_a_POST_request(self):[m
[32m+[m		[32mresponse = self.client.post('/',data={'item_text':'A new list item'})[m
[32m+[m		[32mself.assertIn('A new list item',response.content.decode())[m
 		self.assertTemplateUsed(response,'home.html')[m
\ No newline at end of file[m
[1mdiff --git a/lists/views.py b/lists/views.py[m
[1mindex 218c60c..8737c13 100644[m
[1m--- a/lists/views.py[m
[1m+++ b/lists/views.py[m
[36m@@ -2,4 +2,4 @@[m [mfrom django.shortcuts import render[m
 from django.http import HttpResponse[m
 # Create your views decode[m
 def home_page(request):[m
[31m-	return render(request,'home.html')[m
\ No newline at end of file[m
[32m+[m	[32mreturn render(request,'home.html',{'new_item_text':request.POST.get('item_text',''),})[m
\ No newline at end of file[m
