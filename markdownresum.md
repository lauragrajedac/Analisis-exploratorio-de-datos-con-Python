# [Markdown basic sintax](https://www.markdownguide.org/basic-syntax/#bold-and-italic)

```
# Title 1

## Title 2

### Title 3

#### Title 4

##### Title 5

###### Title 6
```

#### Ejemplo titulo 4

```
**Negritas**
__Bold__
```

**Bold Example**

```
*Cursiva*
_Italic_
```

_Italic Exmaple_

```
***Bold & Italic***
___Negritas & Cursivas___
```

**_Bold & Italic_**

```
* ✨List ✨
  * Subtitle 1
    * Subtitle 2
      * Subtitle 3
O
- ✨List ✨
  - Subtitle 1
    - Subtitle 2
      - Subtitle 3
O
1.-  ✨List ✨
    2.- Subtitulo 1
    * subtitulo 1.1
        3.- Subtitulo 2
        * subtitulo 2.1

```

Ejemplo lista

- ✨List ✨
  - Subtitle 1
    - Subtitle 2
      - Subtitle 3

1.  ✨List ✨  
    2. Subtitulo 1
    - subtitulo 1.1  
       3. Subtitulo 2
      - subtitulo 2.1

```
Blockquotes with Other Elements

> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.

```

> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>   _Everything_ is going according to **plan**.

```
Code Blocks

To denote a word or phrase as code, enclose it in backticks (`).

'print("Hola Mundo")'

To create code blocks, indent every line of the block by at least four spaces or one tab.

    for char in text {
        print(char)
    }

```

### Ejemplo

'print("Hola Mundo")'

    for char in text {
        print(char)
    }

```
URLs and Email Addresses

["Text"]("Path of the page")
<https://www.markdownguide.org>
<fake@example.com>

```

[Link](https://github.com/lauragrajedac)  
<https://www.markdownguide.org>  
<fake@example.com>

```
Para añadir imagenes
!["Nombre"]("Path the la imagen")

```

![Mi foto](unicorn.jpg)

```
Escaping Characters

To display a literal character that would otherwise be used to format text in a Markdown document, add a backslash (\) in front of the character.

\* Without the backslash, this would be a bullet in an unordered list.
```

\* Without the backslash, this would be a bullet in an unordered list.

```
Markdown tambien puede interpretar HTML

<table>
    <tr>
        <th>Nombre</th>
        <th>Apellido</th>
        <th>Edad</th>
    </tr>
    <tr>
        <th>Tom</th>
        <th>Lara</th>
        <th>39</th>
    </tr>
    <tr>
        <th>Lau</th>
        <th>Graciela</th>
        <th>30</th>
    </tr>
</table>
```

<table>
    <tr>
        <th>Nombre</th>
        <th>Apellido</th>
        <th>Edad</th>
    </tr>
    <tr>
        <th>Tom</th>
        <th>Lara</th>
        <th>39</th>
    </tr>
    <tr>
        <th>Lau</th>
        <th>Graciela</th>
        <th>30</th>
    </tr>
</table>
