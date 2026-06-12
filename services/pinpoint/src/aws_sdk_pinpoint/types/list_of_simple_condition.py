"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfSimpleCondition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.simple_condition

ListOfSimpleCondition: TypeAlias = list[
    "aws_sdk_pinpoint.types.simple_condition.SimpleCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfSimpleCondition) -> list:
    import aws_sdk_pinpoint.types.simple_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.simple_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfSimpleCondition:
    import aws_sdk_pinpoint.types.simple_condition

    out: ListOfSimpleCondition = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.simple_condition.deserialize_json(item))
    return out
