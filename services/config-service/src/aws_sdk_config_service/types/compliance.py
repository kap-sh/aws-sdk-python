"""Generated from Smithy shape ``com.amazonaws.configservice#Compliance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.compliance_contributor_count
    import aws_sdk_config_service.types.compliance_type


class Compliance(TypedDict, closed=True):
    compliance_type: NotRequired[
        "aws_sdk_config_service.types.compliance_type.ComplianceType"
    ]
    """<p>Indicates whether an Amazon Web Services resource or Config rule is compliant.</p> <p>A resource is compliant if it complies with all of the Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.</p> <p>A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.</p> <p>Config returns the <code>INSUFFICIENT_DATA</code> value when no evaluation results are available for the Amazon Web Services resource or Config rule.</p> <p>For the <code>Compliance</code> data type, Config supports only <code>COMPLIANT</code>, <code>NON_COMPLIANT</code>, and <code>INSUFFICIENT_DATA</code> values. Config does not support the <code>NOT_APPLICABLE</code> value for the <code>Compliance</code> data type.</p>"""
    compliance_contributor_count: NotRequired[
        "aws_sdk_config_service.types.compliance_contributor_count.ComplianceContributorCount"
    ]
    """<p>The number of Amazon Web Services resources or Config rules that cause a result of <code>NON_COMPLIANT</code>, up to a maximum number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Compliance) -> dict:
    out: dict = {}
    if "compliance_type" in value:
        import aws_sdk_config_service.types.compliance_type

        out["ComplianceType"] = (
            aws_sdk_config_service.types.compliance_type.serialize_aws_json_1_1(
                value["compliance_type"]
            )
        )
    if "compliance_contributor_count" in value:
        import aws_sdk_config_service.types.compliance_contributor_count

        out["ComplianceContributorCount"] = (
            aws_sdk_config_service.types.compliance_contributor_count.serialize_aws_json_1_1(
                value["compliance_contributor_count"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Compliance:
    out: Compliance = {}  # type: ignore[typeddict-item]
    if "ComplianceType" in data:
        import aws_sdk_config_service.types.compliance_type

        out["compliance_type"] = (
            aws_sdk_config_service.types.compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    if "ComplianceContributorCount" in data:
        import aws_sdk_config_service.types.compliance_contributor_count

        out["compliance_contributor_count"] = (
            aws_sdk_config_service.types.compliance_contributor_count.deserialize_aws_json_1_1(
                data["ComplianceContributorCount"]
            )
        )
    return out
