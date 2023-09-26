# What is HTML?

HTML (HyperText Markup Language) is a markup language that tells web browsers how to structure the web pages you visit. It can be as complicated or as simple as the web developer wants it to be. HTML consists of a series of elements, which you use to enclose, wrap, or mark up different parts of content to make it appear or act in a certain way. The enclosing tags can make content into a hyperlink to connect to another page, italicize words, and so on. For example, consider the following line of text:

My cat is very grumpy
If we wanted the text to stand by itself, we could specify that it is a paragraph by enclosing it in a paragraph (<p>) element:

<p>My cat is very grumpy</p>

Note: Tags in HTML are not case-sensitive. This means they can be written in uppercase or lowercase. For example, a <title> tag could be written as <title>, <TITLE>, <Title>, <TiTlE>, etc., and it will work. However, it is best practice to write all tags in lowercase for consistency and readability.

## Anatomy of an HTML element

Let's further explore our paragraph element from the previous section:

A sample code snippet demonstrating the structure of an html element.<p> My cat is very grumpy </p>.

### The anatomy of our element is:

### The opening tag: 

This consists of the name of the element (in this example, p for paragraph), wrapped in opening and closing angle brackets. This opening tag marks where the element begins or starts to take effect. In this example, it precedes the start of the paragraph text.

### The content:

This is the content of the element. In this example, it is the paragraph text.

### The closing tag:

This is the same as the opening tag, except that it includes a forward slash before the element name. This marks where the element ends. Failing to include a closing tag is a common beginner error that can produce peculiar results.

The element is the opening tag, followed by content, followed by the closing tag.

## Nesting elements
Elements can be placed within other elements. This is called nesting. If we wanted to state that our cat is very grumpy, we could wrap the word very in a <strong> element, which means that the word is to have strong(er) text formatting:

<p>My cat is <strong>very</strong> grumpy.</p>

There is a right and wrong way to do nesting. In the example above, we opened the p element first, then opened the strong element. For proper nesting, we should close the strong element first, before closing the p.

The following is an example of the wrong way to do nesting:

<p>My cat is <strong>very grumpy.</p></strong>
The tags have to open and close in a way that they are inside or outside one another. With the kind of overlap in the example above, the browser has to guess at your intent. This kind of guessing can result in unexpected results.

## Void elements
Not all elements follow the pattern of an opening tag, content, and a closing tag. Some elements consist of a single tag, which is typically used to insert/embed something in the document. Such elements are called void elements. For example, the <img> element embeds an image file onto a page:

<img
  src="https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/firefox-icon.png"
  alt="Firefox icon" />
This would output the following:

Note: In HTML, there is no requirement to add a / at the end of a void element's tag, for example: <img src="images/cat.jpg" alt="cat" />. However, it is also a valid syntax, and you may do this when you want your HTML to be valid XML.

## Attributes

Elements can also have attributes. Attributes look like this:

paragraph tag with 'class="editor-note"' attribute emphasized
Attributes contain extra information about the element that won't appear in the content. In this example, the class attribute is an identifying name used to target the element with style information.

An attribute should have:

A space between it and the element name. (For an element with more than one attribute, the attributes should be separated by spaces too.)
The attribute name, followed by an equal sign.
An attribute value, wrapped with opening and closing quote marks.
Active learning: Adding attributes to an element
Another example of an element is <a>. This stands for anchor. An anchor can make the text it encloses into a hyperlink. Anchors can take a number of attributes, but several are as follows:

### href
This attribute's value specifies the web address for the link. For example: href="https://www.mozilla.org/".

### title
The title attribute specifies extra information about the link, such as a description of the page that is being linked to. For example, title="The Mozilla homepage". This appears as a tooltip when a cursor hovers over the element.

### target
The target attribute specifies the browsing context used to display the link. For example, target="_blank" will display the link in a new tab. If you want to display the linked content in the current tab, just omit this attribute.

Add the <a> element.
Add the href attribute and the title attribute.
Specify the target attribute to open the link in the new tab.
You will be able to see your changes live in the Output area. You should see a link—that when hovered over—displays the value of the title attribute and, when clicked, opens a new tab and navigates to the web address in the href attribute. Remember that you need to include a space between the element name and between each attribute.

### Boolean attributes

Sometimes you will see attributes written without values. This is entirely acceptable. These are called Boolean attributes. Boolean attributes can only have one value, which is generally the same as the attribute name. For example, consider the disabled attribute, which you can assign to form input elements. (You use this to disable the form input elements so the user can't make entries. The disabled elements typically have a grayed-out appearance.) For example:

<input type="text" disabled="disabled" />
As shorthand, it is acceptable to write this as follows:

<!-- using the disabled attribute prevents the end user from entering text into the input box -->
<input type="text" disabled />

<!-- text input is allowed, as it doesn't contain the disabled attribute -->
<input type="text" />

For reference, the example above also includes a non-disabled form input element. The HTML from the example above produces this result:

### Omitting quotes around attribute values

If you look at code for a lot of other sites, you might come across a number of strange markup styles, including attribute values without quotes. This is permitted in certain circumstances, but it can also break your markup in other circumstances. For example, if we revisit our link example from earlier, we could write a basic version with only the href attribute, like this:

<a href=https://www.mozilla.org/>favorite website</a>
However, as soon as we add the title attribute in this way, there are problems:

<a href=https://www.mozilla.org/ title=The Mozilla homepage>favorite website</a>

As written above, the browser misinterprets the markup, mistaking the title attribute for three attributes: a title attribute with the value The, and two Boolean attributes, Mozilla and homepage. Obviously, this is not intended! It will cause errors or unexpected behavior, as you can see in the live example below.

Always include the attribute quotes. It avoids such problems, and results in more readable code.

### Single or double quotes?

In this article, you will also notice that the attributes are wrapped in double quotes. However, you might see single quotes in some HTML code. This is a matter of style. You can feel free to choose which one you prefer. Both of these lines are equivalent:

<a href='https://www.example.com'>A link to my example.</a>

<a href="https://www.example.com">A link to my example.</a>

Make sure you don't mix single quotes and double quotes. This example (below) shows a kind of mixing of quotes that will go wrong:

<a href="https://www.example.com'>A link to my example.</a>
However, if you use one type of quote, you can include the other type of quote inside your attribute values:

<a href="https://www.example.com" title="Isn't this fun?">
  A link to my example.
</a>

To use quote marks inside other quote marks of the same type (single quote or double quote), use HTML entities. For example, this will break:

<a href="https://www.example.com" title="An "interesting" reference">A link to my example.</a>
Instead, you need to do this:

<a href="https://www.example.com" title="An &quot;interesting&quot; reference">A link to my example.</a>

### Anatomy of an HTML document
Individual HTML elements aren't very useful on their own. Let's examine how individual elements combine to form an entire HTML page:

<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>

Here we have:

<!DOCTYPE html>: The doctype. When HTML was young (1991-1992), doctypes were meant to act as links to a set of rules that the HTML page had to follow to be considered good HTML. Doctypes used to look something like this:

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
More recently, the doctype is a historical artifact that needs to be included for everything else to work right. 

<!DOCTYPE html> is the shortest string of characters that counts as a valid doctype. That is all you need to know!

<html></html>: The <html> element. This element wraps all the content on the page. It is sometimes known as the root element.

<head></head>: The <head> element. This element acts as a container for everything you want to include on the HTML page, that isn't the content the page will show to viewers. This includes keywords and a page description that would appear in search results, CSS to style content, character set declarations, and more. You will learn more about this in the next article of the series.

<meta charset="utf-8">: The <meta> element. This element represents metadata that cannot be represented by other HTML meta-related elements, like <base>, <link>, <script>, <style> or <title>. The charset attribute specifies the character encoding for your document as UTF-8, which includes most characters from the vast majority of human written languages. With this setting, the page can now handle any textual content it might contain. There is no reason not to set this, and it can help avoid some problems later.

<title></title>: The <title> element. This sets the title of the page, which is the title that appears in the browser tab the page is loaded in. The page title is also used to describe the page when it is bookmarked.

<body></body>: The <body> element. This contains all the content that displays on the page, including text, images, videos, games, playable audio tracks, or whatever else.


No matter how much whitespace you use inside HTML element content (which can include one or more space characters, but also line breaks), the HTML parser reduces each sequence of whitespace to a single space when rendering the code. So why use so much whitespace? The answer is readability.

It can be easier to understand what is going on in your code if you have it nicely formatted.

### Note:

Accessing the innerHTML of elements from JavaScript will keep all the whitespace intact. This may return unexpected results if the whitespace is trimmed by the browser.

Let's have a look at how the browser renders the two paragraphs above with and without whitespace:

const noWhitespace = document.getElementById("noWhitespace").innerHTML;
console.log(noWhitespace);
// "Dogs are silly."

const whitespace = document.getElementById("whitespace").innerHTML;
console.log(whitespace);
// "Dogs
//    are
//        silly."
