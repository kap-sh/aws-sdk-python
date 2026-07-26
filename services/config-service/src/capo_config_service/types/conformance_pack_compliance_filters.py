"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackComplianceFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_compliance_type
    import capo_config_service.types.conformance_pack_config_rule_names


class ConformancePackComplianceFilters(TypedDict, closed=True):
    config_rule_names: NotRequired[
        "capo_config_service.types.conformance_pack_config_rule_names.ConformancePackConfigRuleNames"
    ]
    """<p>Filters the results by Config rule names.</p>"""
    compliance_type: NotRequired[
        "capo_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType"
    ]
    """<p>Filters the results by compliance.</p> <p>The allowed values are <code>COMPLIANT</code> and <code>NON_COMPLIANT</code>. <code>INSUFFICIENT_DATA</code> is not supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackComplianceFilters) -> dict:
    out: dict = {}
    if "config_rule_names" in value:
        import capo_config_service.types.conformance_pack_config_rule_names

        out["ConfigRuleNames"] = (
            capo_config_service.types.conformance_pack_config_rule_names.serialize_aws_json_1_1(
                value["config_rule_names"]
            )
        )
    if "compliance_type" in value:
        import capo_config_service.types.conformance_pack_compliance_type

        out["ComplianceType"] = (
            capo_config_service.types.conformance_pack_compliance_type.serialize_aws_json_1_1(
                value["compliance_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackComplianceFilters:
    out: ConformancePackComplianceFilters = {}  # type: ignore[typeddict-item]
    if "ConfigRuleNames" in data:
        import capo_config_service.types.conformance_pack_config_rule_names

        out["config_rule_names"] = (
            capo_config_service.types.conformance_pack_config_rule_names.deserialize_aws_json_1_1(
                data["ConfigRuleNames"]
            )
        )
    if "ComplianceType" in data:
        import capo_config_service.types.conformance_pack_compliance_type

        out["compliance_type"] = (
            capo_config_service.types.conformance_pack_compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    return out
