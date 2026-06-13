"""Generated from Smithy shape ``com.amazonaws.quicksight#VpcIdRestrictionRuleMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.vpc_id
    import aws_sdk_quicksight.types.vpc_id_restriction_rule_description

VpcIdRestrictionRuleMap: TypeAlias = dict[
    "aws_sdk_quicksight.types.vpc_id.VpcId",
    "aws_sdk_quicksight.types.vpc_id_restriction_rule_description.VpcIdRestrictionRuleDescription",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: VpcIdRestrictionRuleMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> VpcIdRestrictionRuleMap:
    out: VpcIdRestrictionRuleMap = {}
    for key, value in data.items():
        out[key] = value
    return out
