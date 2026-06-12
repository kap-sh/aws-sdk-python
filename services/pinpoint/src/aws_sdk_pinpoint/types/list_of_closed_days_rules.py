"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfClosedDaysRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.closed_days_rule

ListOfClosedDaysRules: TypeAlias = list[
    "aws_sdk_pinpoint.types.closed_days_rule.ClosedDaysRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfClosedDaysRules) -> list:
    import aws_sdk_pinpoint.types.closed_days_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.closed_days_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfClosedDaysRules:
    import aws_sdk_pinpoint.types.closed_days_rule

    out: ListOfClosedDaysRules = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.closed_days_rule.deserialize_json(item))
    return out
