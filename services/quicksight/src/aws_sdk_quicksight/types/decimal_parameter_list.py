"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.decimal_parameter

DecimalParameterList: TypeAlias = list[
    "aws_sdk_quicksight.types.decimal_parameter.DecimalParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DecimalParameterList) -> list:
    import aws_sdk_quicksight.types.decimal_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.decimal_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DecimalParameterList:
    import aws_sdk_quicksight.types.decimal_parameter

    out: DecimalParameterList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.decimal_parameter.deserialize_json(item))
    return out
