"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MatchingRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.matching_rule

MatchingRules: TypeAlias = list[
    "aws_sdk_customer_profiles.types.matching_rule.MatchingRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchingRules) -> list:
    import aws_sdk_customer_profiles.types.matching_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.matching_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchingRules:
    import aws_sdk_customer_profiles.types.matching_rule

    out: MatchingRules = []
    for item in data:
        out.append(aws_sdk_customer_profiles.types.matching_rule.deserialize_json(item))
    return out
