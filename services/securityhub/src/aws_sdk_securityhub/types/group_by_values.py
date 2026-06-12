"""Generated from Smithy shape ``com.amazonaws.securityhub#GroupByValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.group_by_value

GroupByValues: TypeAlias = list["aws_sdk_securityhub.types.group_by_value.GroupByValue"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupByValues) -> list:
    import aws_sdk_securityhub.types.group_by_value

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.group_by_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupByValues:
    import aws_sdk_securityhub.types.group_by_value

    out: GroupByValues = []
    for item in data:
        out.append(aws_sdk_securityhub.types.group_by_value.deserialize_json(item))
    return out
