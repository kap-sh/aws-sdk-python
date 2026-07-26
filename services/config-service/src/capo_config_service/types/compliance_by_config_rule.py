"""Generated from Smithy shape ``com.amazonaws.configservice#ComplianceByConfigRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.compliance
    import capo_config_service.types.string_with_char_limit64


class ComplianceByConfigRule(TypedDict, closed=True):
    config_rule_name: NotRequired[
        "capo_config_service.types.string_with_char_limit64.StringWithCharLimit64"
    ]
    """<p>The name of the Config rule.</p>"""
    compliance: NotRequired["capo_config_service.types.compliance.Compliance"]
    """<p>Indicates whether the Config rule is compliant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceByConfigRule) -> dict:
    out: dict = {}
    if "config_rule_name" in value:
        out["ConfigRuleName"] = value["config_rule_name"]
    if "compliance" in value:
        import capo_config_service.types.compliance

        out["Compliance"] = capo_config_service.types.compliance.serialize_aws_json_1_1(
            value["compliance"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceByConfigRule:
    out: ComplianceByConfigRule = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    if "Compliance" in data:
        import capo_config_service.types.compliance

        out["compliance"] = (
            capo_config_service.types.compliance.deserialize_aws_json_1_1(
                data["Compliance"]
            )
        )
    return out
