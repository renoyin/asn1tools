EXPECTED = {'AllTypes': {'extensibility-implied': False,
              'imports': {},
              'object-classes': {},
              'object-sets': {},
              'types': {'Any': {'type': 'ANY'},
                        'Bitstring': {'type': 'BIT STRING'},
                        'Bitstring2': {'size': [9], 'type': 'BIT STRING'},
                        'Bitstring3': {'size': [(5, 7)], 'type': 'BIT STRING'},
                        'Bitstring4': {'named-bits': [('a', '0'),
                                                      ('b', '1'),
                                                      ('c', '2')],
                                       'type': 'BIT STRING'},
                        'Bitstring5': {'named-bits': [('a', '0'),
                                                      ('b', '1'),
                                                      ('c', '2')],
                                       'size': [(2, 3)],
                                       'type': 'BIT STRING'},
                        'Bmpstring': {'type': 'BMPString'},
                        'Boolean': {'type': 'BOOLEAN'},
                        'Boolean2': {'restricted-to': ['FALSE'],
                                     'type': 'BOOLEAN'},
                        'Boolean3': {'restricted-to': ['TRUE', None],
                                     'type': 'BOOLEAN'},
                        'Choice': {'members': [{'name': 'a',
                                                'type': 'INTEGER'}],
                                   'type': 'CHOICE'},
                        'Enumerated': {'type': 'ENUMERATED',
                                       'values': [('one', 1)]},
                        'Enumerated2': {'type': 'ENUMERATED',
                                        'values': [('one', 1),
                                                   ('two', 2),
                                                   None,
                                                   ('three', 3)]},
                        'GeneralizedTime1': {'type': 'GeneralizedTime'},
                        'Generalstring': {'type': 'GeneralString'},
                        'Graphicstring': {'type': 'GraphicString'},
                        'Ia5string': {'type': 'IA5String'},
                        'Ia5string2': {'from': [('a', 'f'), ('0', '9')],
                                       'type': 'IA5String'},
                        'Ia5string3': {'restricted-to': ['foo',
                                                         'bar',
                                                         'fie',
                                                         '...'],
                                       'type': 'IA5String'},
                        'Ia5string4': {'from': [('0', '2')],
                                       'size': [1],
                                       'type': 'IA5String'},
                        'Integer': {'type': 'INTEGER'},
                        'Integer2': {'restricted-to': [(1, 99)],
                                     'type': 'INTEGER'},
                        'Integer3': {'restricted-to': [(1, 2), (9, 10)],
                                     'type': 'INTEGER'},
                        'Integer4': {'size': [4], 'type': 'INTEGER'},
                        'Integer5': {'type': 'INTEGER'},
                        'Integer6': {'restricted-to': [(4, 7), None],
                                     'type': 'INTEGER'},
                        'List': {'element': {'type': 'INTEGER'},
                                 'type': 'SEQUENCE OF'},
                        'Null': {'type': 'NULL'},
                        'Numericstring': {'type': 'NumericString'},
                        'Objectidentifier': {'type': 'OBJECT IDENTIFIER'},
                        'Octetstring': {'type': 'OCTET STRING'},
                        'Octetstring2': {'size': [2], 'type': 'OCTET STRING'},
                        'Octetstring3': {'size': [3], 'type': 'OCTET STRING'},
                        'Octetstring4': {'size': [(3, 7)],
                                         'type': 'OCTET STRING'},
                        'Octetstring5': {'size': [4, 9],
                                         'type': 'OCTET STRING'},
                        'Printablestring': {'type': 'PrintableString'},
                        'Real': {'type': 'REAL'},
                        'Real10': {'type': 'REAL',
                                   'with-components': [('mantissa',
                                                        (-16777215, 16777215)),
                                                       ('base', 2),
                                                       ('exponent',
                                                        (-149, 104))]},
                        'Real2': {'restricted-to': [('1.0', '2.0')],
                                  'type': 'REAL'},
                        'Real3': {'restricted-to': [(1, 2)], 'type': 'REAL'},
                        'Real4': {'restricted-to': [('1.', 2)], 'type': 'REAL'},
                        'Real5': {'restricted-to': [('1.', 2)], 'type': 'REAL'},
                        'Real6': {'restricted-to': [('-20.0', '-10.0')],
                                  'type': 'REAL'},
                        'Real7': {'tag': {'class': 'UNIVERSAL', 'number': 0},
                                  'type': 'REAL'},
                        'Real8': {'tag': {'class': 'APPLICATION', 'number': 0},
                                  'type': 'REAL'},
                        'Real9': {'tag': {'class': 'PRIVATE', 'number': 0},
                                  'type': 'REAL'},
                        'Sequence': {'members': [], 'type': 'SEQUENCE'},
                        'Sequence10': {'members': [{'name': 'c',
                                                    'type': 'Sequence9',
                                                    'with-components': [None,
                                                                        ('b',
                                                                         'ABSENT')]},
                                                   {'name': 'd',
                                                    'type': 'Sequence9'},
                                                   None],
                                       'type': 'SEQUENCE'},
                        'Sequence11': {'type': 'Sequence10',
                                       'with-components': [['c',
                                                            [{'with-components': [('a',
                                                                                   32)]}],
                                                            'OPTIONAL'],
                                                           ['d']]},
                        'Sequence12': {'members': [{'element': {'type': 'Sequence12'},
                                                    'name': 'a',
                                                    'optional': True,
                                                    'type': 'SEQUENCE OF'}],
                                       'type': 'SEQUENCE'},
                        'Sequence13': {'members': [{'name': 'a',
                                                    'optional': True,
                                                    'tag': {'kind': 'IMPLICIT',
                                                            'number': 0},
                                                    'type': 'List'},
                                                   {'name': 'b',
                                                    'optional': True,
                                                    'tag': {'kind': 'IMPLICIT',
                                                            'number': 1},
                                                    'type': 'List'}],
                                       'type': 'SEQUENCE'},
                        'Sequence14': {'members': [{'name': 'a',
                                                    'tag': {'number': 0},
                                                    'type': 'INTEGER'},
                                                   {'name': 'b',
                                                    'tag': {'number': 1},
                                                    'type': 'Choice'},
                                                   {'name': 'c',
                                                    'tag': {'number': 2},
                                                    'type': 'Sequence9'},
                                                   {'members': [{'name': 'a',
                                                                 'type': 'BOOLEAN'}],
                                                    'name': 'd',
                                                    'tag': {'number': 3},
                                                    'type': 'CHOICE'}],
                                       'type': 'SEQUENCE'},
                        'Sequence15': {'members': [{'default': ['a', 'b'],
                                                    'name': 'a',
                                                    'type': 'Bitstring4'},
                                                   {'default': '0b110',
                                                    'name': 'b',
                                                    'type': 'Bitstring4'},
                                                   {'default': '0xc',
                                                    'name': 'c',
                                                    'type': 'Bitstring4'}],
                                       'type': 'SEQUENCE'},
                        'Sequence16': {'type': 'Sequence9',
                                       'with-components': [('b', 'PRESENT')]},
                        'Sequence17': {'type': 'Sequence9',
                                       'with-components': [('b', 'ABSENT')]},
                        'Sequence18': {'restricted-to': ['Sequence16',
                                                         'Sequence17'],
                                       'type': 'Sequence9'},
                        'Sequence2': {'members': [{'default': 0,
                                                   'name': 'a',
                                                   'type': 'INTEGER'}],
                                      'type': 'SEQUENCE'},
                        'Sequence3': {'members': [{'name': 'a',
                                                   'type': 'BOOLEAN'},
                                                  None],
                                      'type': 'SEQUENCE'},
                        'Sequence4': {'members': [{'name': 'a',
                                                   'type': 'BOOLEAN'},
                                                  None,
                                                  [{'name': 'b',
                                                    'type': 'BOOLEAN'}]],
                                      'type': 'SEQUENCE'},
                        'Sequence5': {'members': [{'name': 'a',
                                                   'type': 'BOOLEAN'},
                                                  None,
                                                  [{'name': 'b',
                                                    'type': 'BOOLEAN'}],
                                                  None],
                                      'type': 'SEQUENCE'},
                        'Sequence6': {'members': [{'name': 'a',
                                                   'type': 'BOOLEAN'},
                                                  None,
                                                  [{'name': 'b',
                                                    'type': 'BOOLEAN'}],
                                                  None,
                                                  {'name': 'c',
                                                   'type': 'BOOLEAN'}],
                                      'type': 'SEQUENCE'},
                        'Sequence7': {'members': [{'name': 'a',
                                                   'type': 'BOOLEAN'},
                                                  None,
                                                  [{'name': 'b',
                                                    'type': 'BOOLEAN'}],
                                                  [{'name': 'c',
                                                    'type': 'BOOLEAN'}],
                                                  None,
                                                  {'name': 'd',
                                                   'type': 'BOOLEAN'}],
                                      'type': 'SEQUENCE'},
                        'Sequence8': {'members': [{'name': 'a',
                                                   'type': 'BOOLEAN'},
                                                  None,
                                                  None],
                                      'type': 'SEQUENCE'},
                        'Sequence9': {'members': [{'name': 'a',
                                                   'type': 'INTEGER'},
                                                  {'name': 'b',
                                                   'optional': True,
                                                   'type': 'BOOLEAN'}],
                                      'type': 'SEQUENCE'},
                        'SequenceOf': {'element': {'type': 'INTEGER'},
                                       'type': 'SEQUENCE OF'},
                        'Set': {'members': [], 'type': 'SET'},
                        'Set2': {'members': [{'default': 1,
                                              'name': 'a',
                                              'type': 'INTEGER'}],
                                 'type': 'SET'},
                        'SetOf': {'element': {'type': 'INTEGER'},
                                  'type': 'SET OF'},
                        'Teletexstring': {'type': 'TeletexString'},
                        'Universalstring': {'type': 'UniversalString'},
                        'Utctime': {'type': 'UTCTime'},
                        'Utf8string': {'type': 'UTF8String'},
                        'Visiblestring': {'type': 'VisibleString'}},
              'values': {'bitstring': {'type': 'BIT STRING',
                                       'value': '0b100010001001'},
                         'bitstring2': {'type': 'BIT STRING',
                                        'value': '0x0123456789abcdef'},
                         'boolean': {'type': 'BOOLEAN', 'value': True},
                         'boolean2': {'type': 'BOOLEAN', 'value': False},
                         'choice': {'type': 'CHOICE', 'value': 'foo'},
                         'foo': {'type': 'INTEGER', 'value': 1},
                         'ia5string': {'type': 'IA5String', 'value': '{'},
                         'ia5string2': {'type': 'IA5String', 'value': '{'}}}}