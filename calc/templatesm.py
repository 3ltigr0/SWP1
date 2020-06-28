html = b"""
<html>
    <body>
        <form action="">
            a: <input type="number" name="a">
            b: <input type="number" name="b">
            <input type="submit">
            <br>
            %s
            <br><br>
        </form>
        <table border = "1">
            <tr>
                <td><b>sum</b></td>
                <td width = "40">%s</td>
            </tr>
            <tr>
                <td><b>mul</b></td>
                <td width = "40">%s</td>
            </tr>
        </table>
    </body>
</html>
"""
