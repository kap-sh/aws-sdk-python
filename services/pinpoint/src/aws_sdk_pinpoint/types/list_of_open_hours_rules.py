"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfOpenHoursRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.open_hours_rule

ListOfOpenHoursRules: TypeAlias = list[
    "aws_sdk_pinpoint.types.open_hours_rule.OpenHoursRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfOpenHoursRules) -> list:
    import aws_sdk_pinpoint.types.open_hours_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.open_hours_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfOpenHoursRules:
    import aws_sdk_pinpoint.types.open_hours_rule

    out: ListOfOpenHoursRules = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.open_hours_rule.deserialize_json(item))
    return out
