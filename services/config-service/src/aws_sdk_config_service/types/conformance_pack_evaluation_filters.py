"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackEvaluationFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_compliance_resource_ids
    import aws_sdk_config_service.types.conformance_pack_compliance_type
    import aws_sdk_config_service.types.conformance_pack_config_rule_names
    import aws_sdk_config_service.types.string_with_char_limit256


class ConformancePackEvaluationFilters(TypedDict):
    config_rule_names: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_config_rule_names.ConformancePackConfigRuleNames"
    ]
    """<p>Filters the results by Config rule names.</p>"""
    compliance_type: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType"
    ]
    """<p>Filters the results by compliance.</p> <p>The allowed values are <code>COMPLIANT</code> and <code>NON_COMPLIANT</code>. <code>INSUFFICIENT_DATA</code> is not supported.</p>"""
    resource_type: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Filters the results by the resource type (for example, <code>\"AWS::EC2::Instance\"</code>). </p>"""
    resource_ids: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_compliance_resource_ids.ConformancePackComplianceResourceIds"
    ]
    """<p>Filters the results by resource IDs.</p> <note> <p>This is valid only when you provide resource type. If there is no resource type, you will see an error.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackEvaluationFilters) -> dict:
    out: dict = {}
    if "config_rule_names" in value:
        import aws_sdk_config_service.types.conformance_pack_config_rule_names

        out["ConfigRuleNames"] = (
            aws_sdk_config_service.types.conformance_pack_config_rule_names.serialize_aws_json_1_1(
                value["config_rule_names"]
            )
        )
    if "compliance_type" in value:
        import aws_sdk_config_service.types.conformance_pack_compliance_type

        out["ComplianceType"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_type.serialize_aws_json_1_1(
                value["compliance_type"]
            )
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_ids" in value:
        import aws_sdk_config_service.types.conformance_pack_compliance_resource_ids

        out["ResourceIds"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_resource_ids.serialize_aws_json_1_1(
                value["resource_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackEvaluationFilters:
    out: ConformancePackEvaluationFilters = {}  # type: ignore[typeddict-item]
    if "ConfigRuleNames" in data:
        import aws_sdk_config_service.types.conformance_pack_config_rule_names

        out["config_rule_names"] = (
            aws_sdk_config_service.types.conformance_pack_config_rule_names.deserialize_aws_json_1_1(
                data["ConfigRuleNames"]
            )
        )
    if "ComplianceType" in data:
        import aws_sdk_config_service.types.conformance_pack_compliance_type

        out["compliance_type"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceIds" in data:
        import aws_sdk_config_service.types.conformance_pack_compliance_resource_ids

        out["resource_ids"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_resource_ids.deserialize_aws_json_1_1(
                data["ResourceIds"]
            )
        )
    return out
