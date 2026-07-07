"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RuleBasedMatchingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_types_selector
    import aws_sdk_customer_profiles.types.conflict_resolution
    import aws_sdk_customer_profiles.types.exporting_config
    import aws_sdk_customer_profiles.types.matching_rules
    import aws_sdk_customer_profiles.types.max_allowed_rule_level_for_matching
    import aws_sdk_customer_profiles.types.max_allowed_rule_level_for_merging
    import aws_sdk_customer_profiles.types.optional_boolean


class RuleBasedMatchingRequest(TypedDict, closed=True):
    enabled: "aws_sdk_customer_profiles.types.optional_boolean.optionalBoolean"
    """<p>The flag that enables the rule-based matching process of duplicate profiles.</p>"""
    matching_rules: NotRequired[
        "aws_sdk_customer_profiles.types.matching_rules.MatchingRules"
    ]
    """<p>Configures how the rule-based matching process should match profiles. You can have up to 15 <code>MatchingRule</code> in the <code>MatchingRules</code>.</p>"""
    max_allowed_rule_level_for_merging: NotRequired[
        "aws_sdk_customer_profiles.types.max_allowed_rule_level_for_merging.MaxAllowedRuleLevelForMerging"
    ]
    r"""<p> <a href=\"https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_MatchingRule.html\">MatchingRule</a> </p>"""
    max_allowed_rule_level_for_matching: NotRequired[
        "aws_sdk_customer_profiles.types.max_allowed_rule_level_for_matching.MaxAllowedRuleLevelForMatching"
    ]
    """<p>Indicates the maximum allowed rule level.</p>"""
    attribute_types_selector: NotRequired[
        "aws_sdk_customer_profiles.types.attribute_types_selector.AttributeTypesSelector"
    ]
    """<p>Configures information about the <code>AttributeTypesSelector</code> where the rule-based identity resolution uses to match profiles.</p>"""
    conflict_resolution: NotRequired[
        "aws_sdk_customer_profiles.types.conflict_resolution.ConflictResolution"
    ]
    exporting_config: NotRequired[
        "aws_sdk_customer_profiles.types.exporting_config.ExportingConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RuleBasedMatchingRequest) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "matching_rules" in value:
        import aws_sdk_customer_profiles.types.matching_rules

        out["MatchingRules"] = (
            aws_sdk_customer_profiles.types.matching_rules.serialize_json(
                value["matching_rules"]
            )
        )
    if "max_allowed_rule_level_for_merging" in value:
        out["MaxAllowedRuleLevelForMerging"] = value[
            "max_allowed_rule_level_for_merging"
        ]
    if "max_allowed_rule_level_for_matching" in value:
        out["MaxAllowedRuleLevelForMatching"] = value[
            "max_allowed_rule_level_for_matching"
        ]
    if "attribute_types_selector" in value:
        import aws_sdk_customer_profiles.types.attribute_types_selector

        out["AttributeTypesSelector"] = (
            aws_sdk_customer_profiles.types.attribute_types_selector.serialize_json(
                value["attribute_types_selector"]
            )
        )
    if "conflict_resolution" in value:
        import aws_sdk_customer_profiles.types.conflict_resolution

        out["ConflictResolution"] = (
            aws_sdk_customer_profiles.types.conflict_resolution.serialize_json(
                value["conflict_resolution"]
            )
        )
    if "exporting_config" in value:
        import aws_sdk_customer_profiles.types.exporting_config

        out["ExportingConfig"] = (
            aws_sdk_customer_profiles.types.exporting_config.serialize_json(
                value["exporting_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleBasedMatchingRequest:
    out: RuleBasedMatchingRequest = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("RuleBasedMatchingRequest.enabled required")
    if "MatchingRules" in data:
        import aws_sdk_customer_profiles.types.matching_rules

        out["matching_rules"] = (
            aws_sdk_customer_profiles.types.matching_rules.deserialize_json(
                data["MatchingRules"]
            )
        )
    if "MaxAllowedRuleLevelForMerging" in data:
        out["max_allowed_rule_level_for_merging"] = data[
            "MaxAllowedRuleLevelForMerging"
        ]
    if "MaxAllowedRuleLevelForMatching" in data:
        out["max_allowed_rule_level_for_matching"] = data[
            "MaxAllowedRuleLevelForMatching"
        ]
    if "AttributeTypesSelector" in data:
        import aws_sdk_customer_profiles.types.attribute_types_selector

        out["attribute_types_selector"] = (
            aws_sdk_customer_profiles.types.attribute_types_selector.deserialize_json(
                data["AttributeTypesSelector"]
            )
        )
    if "ConflictResolution" in data:
        import aws_sdk_customer_profiles.types.conflict_resolution

        out["conflict_resolution"] = (
            aws_sdk_customer_profiles.types.conflict_resolution.deserialize_json(
                data["ConflictResolution"]
            )
        )
    if "ExportingConfig" in data:
        import aws_sdk_customer_profiles.types.exporting_config

        out["exporting_config"] = (
            aws_sdk_customer_profiles.types.exporting_config.deserialize_json(
                data["ExportingConfig"]
            )
        )
    return out
