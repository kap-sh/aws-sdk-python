"""Generated from Smithy shape ``com.amazonaws.appsync#CodeErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.code_error

CodeErrors: TypeAlias = list["aws_sdk_appsync.types.code_error.CodeError"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeErrors) -> list:
    import aws_sdk_appsync.types.code_error

    out: list = []
    for item in value:
        out.append(aws_sdk_appsync.types.code_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeErrors:
    import aws_sdk_appsync.types.code_error

    out: CodeErrors = []
    for item in data:
        out.append(aws_sdk_appsync.types.code_error.deserialize_json(item))
    return out
