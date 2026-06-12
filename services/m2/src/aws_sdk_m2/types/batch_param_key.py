"""Generated from Smithy shape ``com.amazonaws.m2#BatchParamKey``."""

from typing import TypeAlias

"""See https://www.ibm.com/docs/en/workload-automation/9.3.0?topic=zos-coding-variables-in-jcl to get details about limits for both keys and values: 8 for keys (variable names), 44 for values (variable values) In addition, keys will be only alphabetic characters and digits, without any space or special characters (dash, underscore, etc ...) For BluAge Engine: There is no limit in length of keys and values. Additional validation may be applied in code, per engine. Parameter key: the first character must be alphabetic. Can be of up to 32 alphanumeric characters."""
BatchParamKey: TypeAlias = str
