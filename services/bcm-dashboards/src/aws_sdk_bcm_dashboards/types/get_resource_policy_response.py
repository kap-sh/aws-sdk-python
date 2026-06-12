"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.dashboard_arn
    import aws_sdk_bcm_dashboards.types.generic_string


class GetResourcePolicyResponse(TypedDict):
    resource_arn: "aws_sdk_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the dashboard for which the resource-based policy was retrieved.</p>"""
    policy_document: "aws_sdk_bcm_dashboards.types.generic_string.GenericString"
    """<p>The JSON policy document that represents the dashboard's resource-based policy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["policyDocument"] = value["policy_document"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("GetResourcePolicyResponse.resource_arn required")
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    else:
        raise DeserializationError("GetResourcePolicyResponse.policy_document required")
    return out
