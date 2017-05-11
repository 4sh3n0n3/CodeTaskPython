class Creator:
    document = """
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
            self.document = self.document + '<tr>'
            for j in range(1, 11):
                if j == 1:
                    self.document = self.document + '<th>' + str(i) + '</th>'
                else:
                    self.document = self.document + '<td>' + str((j - 1) * i) + '</td>'
            self.document = self.document + '</tr>'
        self.document = self.document + '</table>   </body>   </html>'
        f = open('TableOfMultiplication.html', 'w')
        f.write(self.document)

creator = Creator()
creator.create_table()
