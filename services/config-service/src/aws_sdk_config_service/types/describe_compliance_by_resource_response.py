"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeComplianceByResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.compliance_by_resources
    import aws_sdk_config_service.types.next_token


class DescribeComplianceByResourceResponse(TypedDict, closed=True):
    compliance_by_resources: NotRequired[
        "aws_sdk_config_service.types.compliance_by_resources.ComplianceByResources"
    ]
    """<p>Indicates whether the specified Amazon Web Services resource complies with all of the Config rules that evaluate it.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The string that you use in a subsequent request to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComplianceByResourceResponse) -> dict:
    out: dict = {}
    if "compliance_by_resources" in value:
        import aws_sdk_config_service.types.compliance_by_resources

        out["ComplianceByResources"] = (
            aws_sdk_config_service.types.compliance_by_resources.serialize_aws_json_1_1(
                value["compliance_by_resources"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeComplianceByResourceResponse:
    out: DescribeComplianceByResourceResponse = {}  # type: ignore[typeddict-item]
    if "ComplianceByResources" in data:
        import aws_sdk_config_service.types.compliance_by_resources

        out["compliance_by_resources"] = (
            aws_sdk_config_service.types.compliance_by_resources.deserialize_aws_json_1_1(
                data["ComplianceByResources"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
