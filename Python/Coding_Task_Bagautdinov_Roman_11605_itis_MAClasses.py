class Creator:
    html = """
                  <html>
                  <head>
                    <title>Multiplication Table</title>
                    </head>
                    <body>
                    <table border="5"  align="center"  bgcolor="#808080"  bordercolor="#000000"  cellpadding="3">
                    <caption><h1>Таблица умножения</caption>
                      <tr>
                       <th>a\\b</th>
                        <th>1</th>
                        <th>2</th>
                        <th>3</th>
                        <th>4</th>
                        <th>5</th>
                        <th>6</th>
                        <th>7</th>
                        <th>8</th>
                        <th>9</th>
                      </tr> 
               """

    def create_table(self):
        for i in range(1, 10):
            self.html = self.html + '<tr>'
            for j in range(1, 11):
                if j == 1:
                    self.html = self.html + '<th>' + str(i) + '</th>'
                else:
                    self.html = self.html + '<td>' + str((j - 1) * i) + '</td>'
            self.html = self.html + '</tr>'
        self.html = self.html + '</table>   </body>   </html>'
        f = open('TableOfMultiplication.html', 'w')
        f.write(self.html)

creator = Creator()
creator.create_table()
