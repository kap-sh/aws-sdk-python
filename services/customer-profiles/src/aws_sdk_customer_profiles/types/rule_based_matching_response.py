"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RuleBasedMatchingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_types_selector
    import aws_sdk_customer_profiles.types.conflict_resolution
    import aws_sdk_customer_profiles.types.exporting_config
    import aws_sdk_customer_profiles.types.matching_rules
    import aws_sdk_customer_profiles.types.max_allowed_rule_level_for_matching
    import aws_sdk_customer_profiles.types.max_allowed_rule_level_for_merging
    import aws_sdk_customer_profiles.types.optional_boolean
    import aws_sdk_customer_profiles.types.rule_based_matching_status


class RuleBasedMatchingResponse(TypedDict, closed=True):
    enabled: NotRequired[
        "aws_sdk_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>The flag that enables the rule-based matching process of duplicate profiles.</p>"""
    matching_rules: NotRequired[
        "aws_sdk_customer_profiles.types.matching_rules.MatchingRules"
    ]
    """<p>Configures how the rule-based matching process should match profiles. You can have up to 15 <code>MatchingRule</code> in the <code>MatchingRules</code>.</p>"""
    status: NotRequired[
        "aws_sdk_customer_profiles.types.rule_based_matching_status.RuleBasedMatchingStatus"
    ]
    """<p>PENDING</p> <ul> <li> <p>The first status after configuration a rule-based matching rule. If it is an existing domain, the rule-based Identity Resolution waits one hour before creating the matching rule. If it is a new domain, the system will skip the <code>PENDING</code> stage.</p> </li> </ul> <p>IN_PROGRESS</p> <ul> <li> <p>The system is creating the rule-based matching rule. Under this status, the system is evaluating the existing data and you can no longer change the Rule-based matching configuration.</p> </li> </ul> <p>ACTIVE</p> <ul> <li> <p>The rule is ready to use. You can change the rule a day after the status is in <code>ACTIVE</code>.</p> </li> </ul>"""
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
def serialize_json(value: RuleBasedMatchingResponse) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "matching_rules" in value:
        import aws_sdk_customer_profiles.types.matching_rules

        out["MatchingRules"] = (
            aws_sdk_customer_profiles.types.matching_rules.serialize_json(
                value["matching_rules"]
            )
        )
    if "status" in value:
        import aws_sdk_customer_profiles.types.rule_based_matching_status

        out["Status"] = (
            aws_sdk_customer_profiles.types.rule_based_matching_status.serialize_json(
                value["status"]
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


def deserialize_json(data: dict) -> RuleBasedMatchingResponse:
    out: RuleBasedMatchingResponse = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "MatchingRules" in data:
        import aws_sdk_customer_profiles.types.matching_rules

        out["matching_rules"] = (
            aws_sdk_customer_profiles.types.matching_rules.deserialize_json(
                data["MatchingRules"]
            )
        )
    if "Status" in data:
        import aws_sdk_customer_profiles.types.rule_based_matching_status

        out["status"] = (
            aws_sdk_customer_profiles.types.rule_based_matching_status.deserialize_json(
                data["Status"]
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
