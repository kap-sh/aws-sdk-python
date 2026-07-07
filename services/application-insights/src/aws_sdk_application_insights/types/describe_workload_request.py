"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeWorkloadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.account_id
    import aws_sdk_application_insights.types.component_name
    import aws_sdk_application_insights.types.resource_group_name
    import aws_sdk_application_insights.types.workload_id


class DescribeWorkloadRequest(TypedDict, closed=True):
    resource_group_name: (
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: "aws_sdk_application_insights.types.component_name.ComponentName"
    """<p>The name of the component.</p>"""
    workload_id: "aws_sdk_application_insights.types.workload_id.WorkloadId"
    """<p>The ID of the workload.</p>"""
    account_id: NotRequired["aws_sdk_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the workload owner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkloadRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    out["WorkloadId"] = value["workload_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkloadRequest:
    out: DescribeWorkloadRequest = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        raise DeserializationError(
            "DescribeWorkloadRequest.resource_group_name required"
        )
    if "ComponentName" in data:
        out["component_name"] = data["ComponentName"]
    else:
        raise DeserializationError("DescribeWorkloadRequest.component_name required")
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    else:
        raise DeserializationError("DescribeWorkloadRequest.workload_id required")
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out
