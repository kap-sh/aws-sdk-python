"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.date_time_parameter

DateTimeParameterList: TypeAlias = list[
    "aws_sdk_quicksight.types.date_time_parameter.DateTimeParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeParameterList) -> list:
    import aws_sdk_quicksight.types.date_time_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.date_time_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DateTimeParameterList:
    import aws_sdk_quicksight.types.date_time_parameter

    out: DateTimeParameterList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.date_time_parameter.deserialize_json(item))
    return out
