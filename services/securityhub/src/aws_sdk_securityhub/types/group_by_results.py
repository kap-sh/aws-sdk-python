"""Generated from Smithy shape ``com.amazonaws.securityhub#GroupByResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.group_by_result

GroupByResults: TypeAlias = list[
    "aws_sdk_securityhub.types.group_by_result.GroupByResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupByResults) -> list:
    import aws_sdk_securityhub.types.group_by_result

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.group_by_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupByResults:
    import aws_sdk_securityhub.types.group_by_result

    out: GroupByResults = []
    for item in data:
        out.append(aws_sdk_securityhub.types.group_by_result.deserialize_json(item))
    return out
