"""Generated from Smithy shape ``com.amazonaws.deadline#UsageGroupBy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.usage_group_by_field

UsageGroupBy: TypeAlias = list[
    "aws_sdk_deadline.types.usage_group_by_field.UsageGroupByField"
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageGroupBy) -> list:
    import aws_sdk_deadline.types.usage_group_by_field

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.usage_group_by_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageGroupBy:
    import aws_sdk_deadline.types.usage_group_by_field

    out: UsageGroupBy = []
    for item in data:
        out.append(aws_sdk_deadline.types.usage_group_by_field.deserialize_json(item))
    return out
