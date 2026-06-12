"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfFunctionsResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.function

__listOfFunctionsResponse: TypeAlias = list[
    "aws_sdk_mediatailor.types.function.Function"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfFunctionsResponse) -> list:
    import aws_sdk_mediatailor.types.function

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.function.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfFunctionsResponse:
    import aws_sdk_mediatailor.types.function

    out: __listOfFunctionsResponse = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.function.deserialize_json(item))
    return out
