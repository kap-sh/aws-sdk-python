"""Generated from Smithy shape ``com.amazonaws.configservice#ComplianceSummaryByResourceType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.compliance_summary
    import aws_sdk_config_service.types.string_with_char_limit256


class ComplianceSummaryByResourceType(TypedDict, closed=True):
    resource_type: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The type of Amazon Web Services resource.</p>"""
    compliance_summary: NotRequired[
        "aws_sdk_config_service.types.compliance_summary.ComplianceSummary"
    ]
    """<p>The number of Amazon Web Services resources that are compliant or noncompliant, up to a maximum of 100 for each.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceSummaryByResourceType) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "compliance_summary" in value:
        import aws_sdk_config_service.types.compliance_summary

        out["ComplianceSummary"] = (
            aws_sdk_config_service.types.compliance_summary.serialize_aws_json_1_1(
                value["compliance_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceSummaryByResourceType:
    out: ComplianceSummaryByResourceType = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ComplianceSummary" in data:
        import aws_sdk_config_service.types.compliance_summary

        out["compliance_summary"] = (
            aws_sdk_config_service.types.compliance_summary.deserialize_aws_json_1_1(
                data["ComplianceSummary"]
            )
        )
    return out
