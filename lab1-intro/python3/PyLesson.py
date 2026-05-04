"""
# ---- PYTHON LESSON -----

    Comments: Hash tags for single-lined comment
    Comments: """ or ''' for multi-lined comments, enclose it in either of quotes

# ---- (1) PYTHON INTERACTIVE MODE (Python in Terminal) ----

# -- (1.1) PROMPTS (MATH and DIVISION OPERATORS) --

# (1.1.1) Math
    `number ** power_value` raises number to power of power_value e.g. `number ** 2`, is number squared.
    `2+2` Terminal can calculate expressions and with other operators, + - / etc

# (1.1.2) Division
    Normal division: `number / number` is normal division, returns a floating number.
    Floor division: `number // number` is a floor division, that returns value without fractional part. (Becomes integer)
    Modulo operator: `number % number` is a modulo operator, that returns the remaining part of floating number. (Becomes integer)

# (1.1.3) Extra
    "_" : this operator is where the last result of printed expression is stored. If you manual attach value to it, it overrides the magical feature.
    round(x,y): built-in function that allows to round x to y decimals. For example, `round(2.234, 2)` returns 2.23.
    sum(): built-in function that sums values in a sequence e.g. tuple or list

# -- (1.2) PROMPTS (TEXTS) --

# (1.2.1) Introduction.
    Usage of println: Using variable without print() includes special characters in output, otherwise they are interpreted
    len(variable_name): A built-in function that returns the length of a string

# (1.2.2) Escapes
    Newline: Use `\n` special character to create new line (important to not add space between this and next line)
    Tab: Use `\t` special character to create tab
    Quotes: Use `\` special character to escape quotes or have alternate use of quotes
    Backslash: Use "r" prefix for quote in print() to make `\` not interpreted as a special character. For example, `print(r'C:\this\name')`
    Multi-lined texts: Triple-quoted strings (''' or """) with text enclosed in them create a multi-line text (also known as string literals), it includes newline each time ENTER is pressed; a `\` at the end of a line prevents that newline.

# (1.2.3) Texts (string concatenation)
    String concatenation (part 1): Two string literals written adjacently are automatically concatenated, more explicitly using "+" in-between.
    String concatenation (part 2): Can concatenate variables, or variable and literal using explit string concatenation (+) operator.

# (1.2.4) Texts (string slicing intro)
    A variable containing a string can make the characters indexed into an list, can fetch characters using variable_name[position_in_string] with position_in_string starting from 0.
    - index number can be negative (starting from -1), it will fetch from right to left instead.
    - Invalid positions (exceeding length of word) will produce error. Note, in string slicing error is not produced just an empty string ''

# (1.2.5) Texts (string slicing)
    String slicing: Can obtain substring of a text by adding range inside list. Ranges are split between beginning and end, divided by colon.
    Example 1. variable_name[0:2] lists characters from 0 (including) to 2 (excluding), resulting in two characters listed (positions 0 and 1).
    Example 2. variable_name[:2] lists characters from beginning (including) to 2 (excluding)
    Example 3. variable_name[-2:] lists characters from second-to-last character (including) to end of string (including)
    Example 4. variable_name[:] lists characters from beginning (including) to end of string(including)
    String slicing Note: a colon prefix means from beginning, a colon ending means to end. Ending is always excluded except if it ends with colon.

# (1.2.6) Extra
    - Texts (String slicing) and Texts (string concatenation) link: Two string sliced portions can be concatenated, explicitly with +. For example, `word[:2] + word[2:]`, which makes a new list. 
    - Python strings are cannot be changed (immutable): (pre-read section 1.2.4) leads to error assigning index position in string. Therefore, a new string would need to be created (can use string slicing 1.2.5 and concatenation 1.2.3). Example ` 'J' + word[1:] `.
    - input(string_text): built-in function that prompts user to input answer

# -- (1.3) PROMPTS (LISTS) --

# (1.3.1) Lists (intro)
    Lists are denoted by square brackets [] with items within, comma-separated. The items can be of different types and can be changed, mutable (see 1.3.2).
    Lists can be concatenated (i.e. combined). For example, `squares + [36, 49, 64, 81, 100]`
    len(): Built-in function can be used on lists too, more information in 1.2.1, it identifies number of elements in list

# (1.3.2) Lists (Indexing items)
    You can assign a value at specified index: `variable_name[index] = 64`, the new value at index is 64.
    list_name.append(value): A built-in function that adds items to the end of list_name
    range(): Built-in function that generates a sequence of values. Can be used in list() function to create a list with values.
        - 1 parameter: range(4), number starts from 0 (including) and ends at 4 (excluding)
        - 2 parameters: range(2,4), number starts from 2 (including) and ends at 4 (excluding)
        - 3 parameters: range(0,10,3), refers to (start, end, increments)
        - 3 parameters (alternative): range (-10,-100,-100), refers to (start, end, step)
    Slicing Operation can be used to assign range of indexes value: `variable_name[2:5] = ['C', 'D', 'E']`, or empty it `variable_name[a:b] = []` (clears list by replacing all elements in range with an empty list)

# (1.3.3) Lists (Assigning list to variable)
    Refers to exising list: When you perform normal assignment to variable, variable does not copy data but refers to existing list. See Code below.
        - Changes made to variable containing list will link to other variables refering to same list
    
    ``` CODE BLOCK ```
    rgb = ["Red", "Green", "Blue"]
    rgba = rgb
    print(id(rgb) == id(rgba)) # they reference the same object, prints True.
    rgba.append("Alph")
    print(rgb) # prints ['Red', 'Green', 'Blue', 'Alph']

    Refers to new copy of list: When you assign slice operation to variable, it creates a new list. This concept can be used to create a copy of original list, not performing like normal assignment of list to variable.
    
    ``` CODE BLOCK ```
    correct_rgba = rgba[:]
    correct_rgba[-1] = "Alpha"
    print(correct_rgba) # Prints ["Red", "Green", "Blue", "Alpha"]
    print(rgba) # Prints ["Red", "Green", "Blue", "Alph"]

    Can make nested lists: create lists containing other lists

    ``` CODE BLOCK ```
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n] # x combines separate lists (a and n) into a new list, producing [['a', 'b', 'c'], [1, 2, 3]].

    x in a readable format is:
    [['a', 'b', 'c'], 
    [1, 2, 3]]
    You can extract items using indexes e.g. `x[0]` retuns first row ['a', 'b', 'c']

# -- (1.4) PROMPTS (CONTROL FLOWS) --

# (1.4.1) Control flows (if statements)
    A block of if statement can include: if, multiple elif and else statements.
        - This sequence is used as substitute for switch or case statements found in other languages
    In statements there is an expression (condition), which the program will evaluate to true or false at compilation/runtime

# (1.4.2) Control flows (for statements)
    for loop iterates over items in a sequence (like string or a list, there are more)
        - If intent is modifying collection (e.g. list) as you iterate, recommended to loop over copy of said collection or create a new one (see 1.3.3 for understanding). See below.
    For loop syntax: `for internal_variable in mentioned_sequence:`
    range() : built-in function to generate list of values, can be used as sequence to iterate over
    enumerate() : built-in function supposedly better alternative than range() for iterations
        - produces index and item in iteration
        - first parameter of enumerate is for list, and optionally add second parameter for different start point e.g. `for index, item in enumerate(list_name, start=3)`

    _For Loop Example_
    `users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'} # sample colleciton `

    Strategy 1: Iterate over copy of collection
        - To iterate dictionary copy: `for k,v in dictionary_name.copy().items()`
        - To iterate list copy: `for x in list_name.copy()`

    Strategy 2: Create new collection
        `collection_users = {} # Use for statement techniques in 1.4.2 to iterate over original collection, and use it to populate this new collection `

# (1.4.3) Control flows (break, continue, pass statements)
    break statement: breaks out of innermost for or while loop
        - if no break statement exists in for loop, it enters else clause of the outer loop or block when loop finishes final iteration
        - if no break statement exists in while loop, it enters else clause of the outer loop or block when loop condition becomes false
    continue statement: continues into next iteration of innermost for or while loop
    pass statement: does nothing, used when you want program to take no action and statement required syntatically e.g. while loop or new classes or new functions (optional to define later)
        - Alternatively, any constant expressions can be used as placeholder ("hello", `...`, 5, True): whose value is fixed and does not depend on variables.

# (1.4.4) Control flows (match statements part 1)
    match statement takes an expression and compares the value to different patterns outlined in case blocks. First pattern that matches gets executed, if no case matches, none is executed.
    
    _Match statement syntax_

        ``` CODE BLOCK ```
        def http_error(status):
            match status:
                case 400:
                    return "Bad request"

# (1.4.5) Control flows (match statements part 2)
    Case blocks contain patterns that are checked against a value in a match statement. In this section, we will be exploring different case patterns
        - Case pattern 1 ( _ ): acts as a wildcard and never fails to match (will match anything, so can act as an else case block) e.g. `case _:`
        - Case pattern 2 (OR pattern): "|" notation acts as OR, can be used to match value against multiple alternatives e.g. `case 401 | 403 | 404:`
        - Case pattern 3 (class pattern): matches by type (class) and optionally attributes e.g. `case Point(x=0, y=0):`. More info about class patterns in (1.4.6).
        - Case pattern 4 (sequence patterns): uses square brackets to matches lists or tuples(pairs) e.g. `case [x,y,z]`.
            = In this pattern, ( * ) can be used to capture multiple remaining elements and store it in a variable e.g. `case [x, y, *rest]`, remaining items of list will be contained in rest. Matches sequence of at least two items. MUST use * not **.
            = In this pattern, ( _ ) wildcard with * can be used to ignore captured remaining elements  e.g. `case [x, *_ ]`. Matches sequence of at least one item without binding remaining items.
        - Case pattern 5 (Mapping patterns): uses curly brackets with key and value items to match dictionaries e.g. `{"bandwidth": b, "latency": 1}`. 
            = In this pattern, ( ** ) can be used to capture remaining key and value pairs e.g. `**rest` and it will be stored in rest. MUST use **, not *.
            = In this pattern, ( _ ) wildcard with * is still supported but redundant as you can just exclude pairs you do not want from within the pattern.
            
            There are different cases for how this could be satisfied:
            - `case {"bandwidth":b}` : matches if "bandwidth" key exists and assigns the value to b
            - `case {"bandwidth": 50}` : matches only if key exists and value equals to 50
            - `case {"bandwidth":b, **rest}` : matches if "bandwidth" key exists and stores value in v, and collects other keys-value pairs into rest

        - Case pattern 6 (Literal pattern): matches exact value e.g. `case 5`, python checks equality, using == to evaluate if match value matches case value. Applies to strings and other literals.
        - Case pattern 7 (Variable pattern): matches anything and assigns it to variable e.g. `case x`, in this case, variable x
        - Case pattern 8 (Singleton pattern): matches exact singletons e.g. `case True`, `case False` or `case None`; does not consider truthy or falsy (e.g. 1 or 0) because they are compared by identity ("is" keyword) than equality (== operation)
        - Case pattern 9 (Constant pattern): matches a fixed, named value like constant.HEIGHT or Color.RED
            = To make a constant you can reference, define it in a separate module (e.g. constants.py) and import it — then use it as constants.HEIGHT in your case.
            = They must use dotted names so Python recognizes them as constants, bare names like `case HEIGHT:` are treated as variable captures.
            
    Case block contains pattern modifiers (they control/refine the match):
        - Case block "Guards": A guard is an if clause that gets executed after match, filters matches by doing an additional test
        - Case block "As" Keywords: It captures the whole match case e.g. `case [x,y] as pair`, will result in pair if printed outputting '[x,y]'

    Unpacking operators (* and **): * is just for sequences and ** is for dictionaries, typically stored in rest variable e.g. `**rest` but other names are allowed.

# (1.4.6) Control flows (Intro to class patterns)
    In a case block, class patterns match against instances of your own classes and optionally their attributes

    ``` CODE BLOCK ```
    class Point:
        __match_args__ = ("x","y")

        def __init__(self,x,y):
            self.x = x
            self.y = y

# (1.4.7) Control flows (Intro to class patterns : Matching against attributes of a class)

    _Keyword pattern_
    format: `case Point(x=a, y=b)`
    A keyword pattern explicitly names the attributes that you want to match.
    - When __match_args__ is not defined in the class keyword patterns must be used.
    - Python looks up the attributes x and y on the object and reads their values.

    _Positional pattern_
    format: `case Point(a, b)`
    A positional pattern just gives the values — the attribute names are implicit, inferred from __match_args__
    - When the special attribute __match_args__ is defined in a class, it maps positional pattern arguments to existing attribute names.
    - __match_args__ tells Python what attribute name correspond to which positional argument. Python checks if object has the attributes named in __match_args__ and reads their values.
    Benefits of __match_args__: makes the class pattern shorter

# -- (1.5) SPECIAL PARTS OF PROMPT --
    ( _ ) Wildcard : has many functionality (see 1.1.3 , 1.4.5, ) COMPLETE THIS SECTION!
    len(): mentioned in 1.2.1 and 1.3.1
    ( * and ** ) Unpacking operator: More on this in (1.4.5). If used in function definition, it will mean to collect all positional arguments into tuple or into key-value dictionary e.g. def function(*args), in this case, tuple within variable args.

"""
