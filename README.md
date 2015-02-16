# PirateTranslator
created english-pirate translator app using HTML, CSS, Python, and Flask

Summary
---
Simple app with only a few pages:
- Home
- Game page (takes input)
- Results page (shows output)
  Asks to play again (routes back to Home or to Goodbye)
- Goodbye

This allows me to become more familiar with Flask and routing pages back and forth. It also allows
Getting Set Up
---
Create and activate a new, empty virtual environment.

`virtualenv env`
`source env/bin/activate`

Use pip to install the packages required in requirements.txt (full tutorial on pip/virtualenv)

`pip install -r requirements.txt`

Start the application by running python melons.py.
Navigate to http://localhost:5000 and start exploring the app.

How to Explore
---
Input sentence that will be translated. Translating dictionary and code in:

`pirate_gen.py`

Shows the original input and translated result.

Allows for multi-play by routing you back to the homepage or to an exit page.

Your first task is to explore the app from within your browser. The goal is to understand how the app is laid out. For each page, try to identify the following (and write it down somewhere)

The controller function attached to each page
The model function calls (if any) for a given page
The template for a page
As you do this, watch out for a number of specific things.

Variable Names in Templates

Try to make sure you understand the source of all the variables that are being used in the .html templates. Whenever you see a {{ var }} in a template, make sure that you can match the variable listed with one coming from your model.

The Melon Detail Template

You'll notice that the melon detail page uses an {% if %} statement to display whether or not a given melon is seedless. Remember this syntax from our earlier Jinja lesson. In addition to giving us a mechanism for inserting placeholders into our HTML, it also gives us a few control structures, like if-statements and for-loops. We can use this to make the contents of our page a little more dynamic.

Jinja if-statement documentation

The Melon List Template

The template for our melon list has an example of a Jinja {% for %} loop as well.

Jinja for-loop documentation

Sparse Templates

You'll see that some of the provided templates are very sparse. This is because for the most part, each page has the same HTML as all the other pages. In the spirit of not repeating ourselves, Jinja provides a mechanism to take the common parts of a template out and move it to a 'skeleton' template that is shared across pages. In our case, the skeleton is base.html. As you fix various bugs, you may find that some of the bugs reside in the base template and not the page template.

Jinja template inheritance documentation

Static Files

If you try to access the html templates directly in your browser, ie: navigate over to http://localhost:5000/templates/all_melons.html, you will get a 404 error. This is because templates have to be preprocessed before they can be displayed. They have to be run through a controller for all the placeholder variables to be replaced.

However, you can access http://localhost:5000/static/img/ubermelonsmall.png without any issue. This is because the ubermelon logo resides in a special directory called static. Files that go in this directory are available to the browser without any preprocessing. This makes sense for files like images or stylesheets that don't change: static files.

The Checkout Button

Checking out our shopping cart is outside the scope of our task, but it is worth noting the 'message flash' mechanism that is used when you try to check out. It is a way to display one-time messages to the user. This is a great place to place error, warning, or success messages. Flashed messages only display once, if you reload the page, you will see that it disappears on the second view.

Flask Message Flashing documentation

Styling

Most of the style work in our app was not written manually. Instead, we used bootstrap, a css framework. The bootstrap framework specifies 'components', higher level UI components composed of more basic HTML tags. Notably, we use the navbar component and the well component.

Bootstrap component list

Task 2: The Login Page

If you click on the 'Log In' link in the nav bar at the top of the screen, you'll see that it does nothing. However, if you peruse the list of routes available in your melons.py file, you will find that there is a login route that is inaccessible by clicking. You can, however, browse on over to the URL directly in your browser.

Fixing this bug

Wire up the link to go to the page.

Your first task is to locate the <a href> tag that is used in the black bar at the top of the page. This section of the page is typically called the navbar. It may be tricky at first to find where in the code this tag exists. Remember to use the browser's element inspector to see exactly what lines of HTML you're looking for. Also remember that this part of the page is shared across multiple pages.

Style the page.

When you do have the login page 'wired up', you'll notice that it's styled pretty terribly. We want it to use the same style as all the other pages. We could try to add bootstrap to the HTML directly, but it is easier to make this page a child of our base.html template. Check either melon_details.html or all_melons.html for an example on how to do that.

Task 3: The Melon Cart Icon

The melon cart link at the top of the page has a broken image. If you browse around our directory tree, you'll find that the file exists, but isn't linked properly.

Fixing this bug

First, fix the link.

Make sure you understand why it's not displaying in the first place.

Style this component.

Find the stylesheet that's being used and fiddle with the style to make it display correctly. A height of 15px on this image should do it. Try to figure out a CSS selector that targets just that image without affecting others. Here's a css selector guide if you need help.

Task 4: The Melon Cart Functionality

When you view the shopping cart, you'll notice that all the items in it are placeholder dummy items. We'll need to replace these items with actual melons. In addition, the 'Add to Cart' button on the melon detail page is wired up but the controller currently doesn't do anything.

We need a way to temporarily hold information that the user generates (ie: which melons are in the cart). We could commit this to the database, but this isn't long-term information, nor is it information that's attached to any particular user. It's short-term information that's attached to the browser you're currently using. This kind of information is best stored in a storage mechanism called 'the session'. We will use the session to carry information from clicking the 'Add to Cart' button all the way to the shopping cart page.

Read the Session documentation to figure out how to import session from Flask and use it (hint: look for where we define a secret key, and once everything is set up, try to put something in the session and then print it out).

Implementing a Cart Feature using the Session

This feature is two-part. The order in which you build the feature doesn't matter, but it may be helpful to write both in conjunction.

Add things to the cart.

When you click the add to cart button, the fact that a melon has been added to a "cart" needs to be recorded somewhere. Breaking down the process, here are the necessary pieces:

On adding an item, check to see if the session contains a cart already
If not, add a new cart (an empty list) to the session
Append the melon id under consideration to our cart list
Flash a message indicating the melon was successfully added to the cart
Redirect the user to the shopping cart page
Display the cart contents.

Displaying the contents of the cart is a little simpler, but is an exercise in fiddling with Jinja templates and HTML tags. Essentially, in our shopping cart page, we will loop through all the melons in our cart and display them in a table.

In our cart controller, get a list of melon ids in the cart out of the session (if it exists)
Query the database for all melons that match the ids in the list
Pass the list of melons on to the shopping cart template
In the shopping cart template, delete the placeholder rows
Use a jinja for loop to iterate through the melon list, outputting each melon to the table in place of the original placeholders.
With each part of the feature being reasonably complex, it makes sense to do them in stages. For example, you might go through this sequence instead:

On adding an item, add some arbitrary string to the session
In the shopping cart page, add some code to display the string from the session.
Going back to the add_to_cart controller, replace the string with the actual melon object
Going back to the shopping cart page, rewrite the page to display the single melon object
In the add_to_cart controller, replace the single melon with a melon list...
And so on.

