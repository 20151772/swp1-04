html = """
<html>
	<body>
		<form action="">
			<h3>a:</h3>
			<input type="number" name="a"><br>
			<h3>b:</h3>
			<input type="number" name="b"></h3><br><br>
			<input type="submit"><br>	
		</form>
		<h3>a + b = %(sum)s </h3>
		<h3>a * b = %(multi)s </h3>
		<br><center><h3> %(err_msg)s </h3></center>
	</body>
</html>
"""
