"""Generated from Smithy shape ``com.amazonaws.quicksight#VpcEndpointIdRestrictionRuleMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.vpc_endpoint_id
    import aws_sdk_quicksight.types.vpc_endpoint_id_restriction_rule_description

VpcEndpointIdRestrictionRuleMap: TypeAlias = dict[
    "aws_sdk_quicksight.types.vpc_endpoint_id.VpcEndpointId",
    "aws_sdk_quicksight.types.vpc_endpoint_id_restriction_rule_description.VpcEndpointIdRestrictionRuleDescription",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: VpcEndpointIdRestrictionRuleMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> VpcEndpointIdRestrictionRuleMap:
    out: VpcEndpointIdRestrictionRuleMap = {}
    for key, value in data.items():
        out[key] = value
    return out
