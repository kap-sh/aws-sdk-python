"""Generated from Smithy shape ``com.amazonaws.quicksight#IpRestrictionRuleMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.cidr
    import aws_sdk_quicksight.types.ip_restriction_rule_description

IpRestrictionRuleMap: TypeAlias = dict[
    "aws_sdk_quicksight.types.cidr.CIDR",
    "aws_sdk_quicksight.types.ip_restriction_rule_description.IpRestrictionRuleDescription",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: IpRestrictionRuleMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> IpRestrictionRuleMap:
    out: IpRestrictionRuleMap = {}
    for key, value in data.items():
        out[key] = value
    return out
