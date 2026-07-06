"""Generated from Smithy shape ``com.amazonaws.configservice#ComplianceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.compliance_contributor_count
    import aws_sdk_config_service.types.date


class ComplianceSummary(TypedDict, closed=True):
    compliant_resource_count: NotRequired[
        "aws_sdk_config_service.types.compliance_contributor_count.ComplianceContributorCount"
    ]
    """<p>The number of Config rules or Amazon Web Services resources that are compliant, up to a maximum of 25 for rules and 100 for resources.</p>"""
    non_compliant_resource_count: NotRequired[
        "aws_sdk_config_service.types.compliance_contributor_count.ComplianceContributorCount"
    ]
    """<p>The number of Config rules or Amazon Web Services resources that are noncompliant, up to a maximum of 25 for rules and 100 for resources.</p>"""
    compliance_summary_timestamp: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time that Config created the compliance summary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceSummary) -> dict:
    out: dict = {}
    if "compliant_resource_count" in value:
        import aws_sdk_config_service.types.compliance_contributor_count

        out["CompliantResourceCount"] = (
            aws_sdk_config_service.types.compliance_contributor_count.serialize_aws_json_1_1(
                value["compliant_resource_count"]
            )
        )
    if "non_compliant_resource_count" in value:
        import aws_sdk_config_service.types.compliance_contributor_count

        out["NonCompliantResourceCount"] = (
            aws_sdk_config_service.types.compliance_contributor_count.serialize_aws_json_1_1(
                value["non_compliant_resource_count"]
            )
        )
    if "compliance_summary_timestamp" in value:
        import aws_sdk_config_service.types.date

        out["ComplianceSummaryTimestamp"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["compliance_summary_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceSummary:
    out: ComplianceSummary = {}  # type: ignore[typeddict-item]
    if "CompliantResourceCount" in data:
        import aws_sdk_config_service.types.compliance_contributor_count

        out["compliant_resource_count"] = (
            aws_sdk_config_service.types.compliance_contributor_count.deserialize_aws_json_1_1(
                data["CompliantResourceCount"]
            )
        )
    if "NonCompliantResourceCount" in data:
        import aws_sdk_config_service.types.compliance_contributor_count

        out["non_compliant_resource_count"] = (
            aws_sdk_config_service.types.compliance_contributor_count.deserialize_aws_json_1_1(
                data["NonCompliantResourceCount"]
            )
        )
    if "ComplianceSummaryTimestamp" in data:
        import aws_sdk_config_service.types.date

        out["compliance_summary_timestamp"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["ComplianceSummaryTimestamp"]
            )
        )
    return out
