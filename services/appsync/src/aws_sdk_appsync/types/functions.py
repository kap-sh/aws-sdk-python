"""Generated from Smithy shape ``com.amazonaws.appsync#Functions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.function_configuration

Functions: TypeAlias = list[
    "aws_sdk_appsync.types.function_configuration.FunctionConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: Functions) -> list:
    import aws_sdk_appsync.types.function_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_appsync.types.function_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> Functions:
    import aws_sdk_appsync.types.function_configuration

    out: Functions = []
    for item in data:
        out.append(aws_sdk_appsync.types.function_configuration.deserialize_json(item))
    return out
