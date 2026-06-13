"""Generated from Smithy shape ``com.amazonaws.quicksight#IntegerParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.integer_parameter

IntegerParameterList: TypeAlias = list[
    "aws_sdk_quicksight.types.integer_parameter.IntegerParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegerParameterList) -> list:
    import aws_sdk_quicksight.types.integer_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.integer_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntegerParameterList:
    import aws_sdk_quicksight.types.integer_parameter

    out: IntegerParameterList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.integer_parameter.deserialize_json(item))
    return out
