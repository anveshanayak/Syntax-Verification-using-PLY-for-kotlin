import warnings
warnings.filterwarnings("ignore")
import ply.lex as lex
import ply.yacc as yacc

tokens = ['ID',
          'NUMBER',
          'QUOTE2',
          'QUOTE1',
          'ASSIGN',
          'L_PARENTHESIS',
          'R_PARENTHESIS',
          'L_CURLY',
          'R_CURLY',
          'SEMICOLON',
          'NEWLINE',
          'EQUALS',
          'GREATER_THAN_OR_EQUAL_TO',
          'LESSER_THAN_OR_EQUAL_TO',
          'GREATER_THAN',
          'LESSER_THAN',
          'NOT_EQUALS'
          ]


reserved = {
    'fun': 'fun',
    'main': 'main',
    'var': 'var',
    'val': 'val',
    'do': 'do',
    'while': 'while',
    'statements': 'statements',
    'for': 'for',
    'in': 'in',
    'println': 'println',
    'string': 'string'
    }

t_ignore = r" "
t_QUOTE2 = r'\"'
t_QUOTE1 = r"\'"
t_ASSIGN = r'\='
t_NEWLINE=r"\n"
t_SEMICOLON=r"\;"
t_L_PARENTHESIS=r"\("
t_R_PARENTHESIS=r"\)"
t_L_CURLY=r"\{"
t_R_CURLY=r"\}"
t_EQUALS = r'\=='
t_NOT_EQUALS = r'\!='
t_GREATER_THAN_OR_EQUAL_TO = r'\>='
t_LESSER_THAN_OR_EQUAL_TO = r'\<='
t_GREATER_THAN = r'\>'
t_LESSER_THAN = r'\<'
t_while = r'while'
t_statements = r'statements'
t_var = r'var'
t_val = r'val'
t_fun = r'fun'
t_main = r'main'
t_for = r'for'
t_in = r'in'
t_println = r'println'
t_do = r'do'
t_string =r'string'


tokens += list(reserved.values())

def t_NUMBER(t):
   r'\d+'
   t.value=int(t.value)
   return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def p_program(p):
    '''program : fun main L_PARENTHESIS R_PARENTHESIS L_CURLY NEWLINE code NEWLINE R_CURLY'''
    print("Syntax is correct .")

def p_code(p):
    '''code : val assign_expr
           | var assign_expr
           | println print_expr
           | while while_expr
           | for for_expr
           | do statementsub NEWLINE while do_while_expr
           |'''


def p_assign_expr(p):
    '''assign_expr : ID ASSIGN QUOTE2 ID QUOTE2
            | ID ASSIGN QUOTE1 ID QUOTE1
            | ID ASSIGN ID
            | ID ASSIGN NUMBER'''


def p_while_expr(p):
    '''while_expr : L_PARENTHESIS condition R_PARENTHESIS statementsub'''


def p_for_expr(p):
    '''for_expr : L_PARENTHESIS for_condition R_PARENTHESIS statementsub'''


def p_do_while_expr(p):
    '''do_while_expr : L_PARENTHESIS condition R_PARENTHESIS SEMICOLON'''


def p_print_expr(p):
    '''print_expr : L_PARENTHESIS QUOTE2 string QUOTE2 R_PARENTHESIS
            | L_PARENTHESIS QUOTE1 string QUOTE1 R_PARENTHESIS
            | L_PARENTHESIS ID R_PARENTHESIS
            | L_PARENTHESIS NUMBER R_PARENTHESIS'''


def p_condition(p):
    '''condition : ID EQUALS ID
                | ID NOT_EQUALS ID
                | ID GREATER_THAN_OR_EQUAL_TO ID
                | ID LESSER_THAN_OR_EQUAL_TO ID
                | ID GREATER_THAN ID
                | ID LESSER_THAN ID
                | ID EQUALS NUMBER
                | ID NOT_EQUALS NUMBER
                | ID GREATER_THAN_OR_EQUAL_TO NUMBER
                | ID LESSER_THAN_OR_EQUAL_TO NUMBER
                | ID GREATER_THAN NUMBER
                | ID LESSER_THAN NUMBER
                | NUMBER EQUALS ID
                | NUMBER NOT_EQUALS ID
                | NUMBER GREATER_THAN_OR_EQUAL_TO ID
                | NUMBER LESSER_THAN_OR_EQUAL_TO ID
                | NUMBER GREATER_THAN ID
                | NUMBER LESSER_THAN ID
                '''

def p_for_condition(p):
    '''for_condition : ID in ID'''


def p_statementsub(p):
    '''statementsub : L_CURLY NEWLINE statements NEWLINE R_CURLY
                    | L_CURLY NEWLINE code NEWLINE R_CURLY'''

def p_error(p):
  print("Syntax error.");


def t_error(p):
    print("Syntax incorrect");


lex.lex()
yacc.yacc()

data = '''fun main(){
    val a = 10
}'''
data2 = '''fun main(){
    println("string")
}'''

data3 = '''fun main(){
    for(x in vars){
    statements
    }
}'''

data4 = '''fun main(){
    while(x<0){
    val a = 0
    }
}'''

data5 = '''fun main(){
    do{
    do{
    val a = 10
    }
    while(x>0);
    }
    while(x>0);
}'''

data6 = '''fun main(){
    do{
    do{
    val a = 10
    }
    while(x>0);
    }
    while(x>0);
}'''

data7 = '''fun main(){

}'''

print('variable declaration:')
yacc.parse(data)

print()
print('print statement')
yacc.parse(data2)

print()
print('for statement')
yacc.parse(data3)

print()
print('while statement')
yacc.parse(data4)

print()
print('do while statement')
yacc.parse(data5)

print()
print('nested statement')
yacc.parse(data6)


