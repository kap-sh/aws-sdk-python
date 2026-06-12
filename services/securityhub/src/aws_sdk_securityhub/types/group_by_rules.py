"""Generated from Smithy shape ``com.amazonaws.securityhub#GroupByRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.group_by_rule

GroupByRules: TypeAlias = list["aws_sdk_securityhub.types.group_by_rule.GroupByRule"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupByRules) -> list:
    import aws_sdk_securityhub.types.group_by_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.group_by_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupByRules:
    import aws_sdk_securityhub.types.group_by_rule

    out: GroupByRules = []
    for item in data:
        out.append(aws_sdk_securityhub.types.group_by_rule.deserialize_json(item))
    return out
