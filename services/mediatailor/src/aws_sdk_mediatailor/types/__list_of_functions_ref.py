"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfFunctionsRef``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.function_ref

__listOfFunctionsRef: TypeAlias = list[
    "aws_sdk_mediatailor.types.function_ref.FunctionRef"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfFunctionsRef) -> list:
    import aws_sdk_mediatailor.types.function_ref

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.function_ref.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfFunctionsRef:
    import aws_sdk_mediatailor.types.function_ref

    out: __listOfFunctionsRef = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.function_ref.deserialize_json(item))
    return out
