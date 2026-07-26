"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MatchingRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.matching_rule

MatchingRules: TypeAlias = list[
    "capo_customer_profiles.types.matching_rule.MatchingRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchingRules) -> list:
    import capo_customer_profiles.types.matching_rule

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.matching_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> MatchingRules:
    import capo_customer_profiles.types.matching_rule

    out: MatchingRules = []
    for item in data:
        out.append(capo_customer_profiles.types.matching_rule.deserialize_json(item))
    return out
