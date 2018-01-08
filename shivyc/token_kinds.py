"""The token kinds currently recognized."""

from shivyc.tokens import TokenKind

keyword_kinds = []
symbol_kinds = []

# Until function definition is ready, we define `main` as a hardcoded keyword
main = TokenKind("main", keyword_kinds)

bool_kw = TokenKind("_Bool", keyword_kinds)
char_kw = TokenKind("char", keyword_kinds)
short_kw = TokenKind("short", keyword_kinds)
int_kw = TokenKind("int", keyword_kinds)
long_kw = TokenKind("long", keyword_kinds)
signed_kw = TokenKind("signed", keyword_kinds)
unsigned_kw = TokenKind("unsigned", keyword_kinds)
void_kw = TokenKind("void", keyword_kinds)

return_kw = TokenKind("return", keyword_kinds)
if_kw = TokenKind("if", keyword_kinds)
else_kw = TokenKind("else", keyword_kinds)
while_kw = TokenKind("while", keyword_kinds)
for_kw = TokenKind("for", keyword_kinds)
break_kw = TokenKind("break", keyword_kinds)
continue_kw = TokenKind("continue", keyword_kinds)

auto_kw = TokenKind("auto", keyword_kinds)
static_kw = TokenKind("static", keyword_kinds)
extern_kw = TokenKind("extern", keyword_kinds)
struct_kw = TokenKind("struct", keyword_kinds)

plus = TokenKind("+", symbol_kinds)
minus = TokenKind("-", symbol_kinds)
star = TokenKind("*", symbol_kinds)
slash = TokenKind("/", symbol_kinds)
mod = TokenKind("%", symbol_kinds)
incr = TokenKind("++", symbol_kinds)
decr = TokenKind("--", symbol_kinds)
equals = TokenKind("=", symbol_kinds)
plusequals = TokenKind("+=", symbol_kinds)
minusequals = TokenKind("-=", symbol_kinds)
starequals = TokenKind("*=", symbol_kinds)
divequals = TokenKind("/=", symbol_kinds)
modequals = TokenKind("%=", symbol_kinds)
twoequals = TokenKind("==", symbol_kinds)
notequal = TokenKind("!=", symbol_kinds)
bool_and = TokenKind("&&", symbol_kinds)
bool_or = TokenKind("||", symbol_kinds)
bool_not = TokenKind("!", symbol_kinds)
lt = TokenKind("<", symbol_kinds)
gt = TokenKind(">", symbol_kinds)
amp = TokenKind("&", symbol_kinds)
pound = TokenKind("#", symbol_kinds)

dquote = TokenKind('"', symbol_kinds)
squote = TokenKind("'", symbol_kinds)

open_paren = TokenKind("(", symbol_kinds)
close_paren = TokenKind(")", symbol_kinds)
open_brack = TokenKind("{", symbol_kinds)
close_brack = TokenKind("}", symbol_kinds)
open_sq_brack = TokenKind("[", symbol_kinds)
close_sq_brack = TokenKind("]", symbol_kinds)

comma = TokenKind(",", symbol_kinds)
semicolon = TokenKind(";", symbol_kinds)
dot = TokenKind(".", symbol_kinds)
arrow = TokenKind("->", symbol_kinds)

identifier = TokenKind()
number = TokenKind()
string = TokenKind()
char_string = TokenKind()
include_file = TokenKind()
