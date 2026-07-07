"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackRuleCompliance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule_name
    import aws_sdk_config_service.types.conformance_pack_compliance_type
    import aws_sdk_config_service.types.controls_list


class ConformancePackRuleCompliance(TypedDict, closed=True):
    config_rule_name: NotRequired[
        "aws_sdk_config_service.types.config_rule_name.ConfigRuleName"
    ]
    """<p>Name of the Config rule.</p>"""
    compliance_type: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType"
    ]
    """<p>Compliance of the Config rule.</p>"""
    controls: NotRequired["aws_sdk_config_service.types.controls_list.ControlsList"]
    """<p>Controls for the conformance pack. A control is a process to prevent or detect problems while meeting objectives. A control can align with a specific compliance regime or map to internal controls defined by an organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackRuleCompliance) -> dict:
    out: dict = {}
    if "config_rule_name" in value:
        out["ConfigRuleName"] = value["config_rule_name"]
    if "compliance_type" in value:
        import aws_sdk_config_service.types.conformance_pack_compliance_type

        out["ComplianceType"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_type.serialize_aws_json_1_1(
                value["compliance_type"]
            )
        )
    if "controls" in value:
        import aws_sdk_config_service.types.controls_list

        out["Controls"] = (
            aws_sdk_config_service.types.controls_list.serialize_aws_json_1_1(
                value["controls"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackRuleCompliance:
    out: ConformancePackRuleCompliance = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    if "ComplianceType" in data:
        import aws_sdk_config_service.types.conformance_pack_compliance_type

        out["compliance_type"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    if "Controls" in data:
        import aws_sdk_config_service.types.controls_list

        out["controls"] = (
            aws_sdk_config_service.types.controls_list.deserialize_aws_json_1_1(
                data["Controls"]
            )
        )
    return out
