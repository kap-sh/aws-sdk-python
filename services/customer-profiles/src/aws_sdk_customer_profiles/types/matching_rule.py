"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MatchingRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.matching_rule_attribute_list


class MatchingRule(TypedDict, closed=True):
    rule: "aws_sdk_customer_profiles.types.matching_rule_attribute_list.MatchingRuleAttributeList"
    """<p>A single rule level of the <code>MatchRules</code>. Configures how the rule-based matching process should match profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchingRule) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.matching_rule_attribute_list

    out["Rule"] = (
        aws_sdk_customer_profiles.types.matching_rule_attribute_list.serialize_json(
            value["rule"]
        )
    )
    return out


def deserialize_json(data: dict) -> MatchingRule:
    out: MatchingRule = {}  # type: ignore[typeddict-item]
    if "Rule" in data:
        import aws_sdk_customer_profiles.types.matching_rule_attribute_list

        out["rule"] = (
            aws_sdk_customer_profiles.types.matching_rule_attribute_list.deserialize_json(
                data["Rule"]
            )
        )
    else:
        raise DeserializationError("MatchingRule.rule required")
    return out
