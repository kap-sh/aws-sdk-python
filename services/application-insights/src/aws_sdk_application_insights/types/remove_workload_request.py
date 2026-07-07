"""Generated from Smithy shape ``com.amazonaws.applicationinsights#RemoveWorkloadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.component_name
    import aws_sdk_application_insights.types.resource_group_name
    import aws_sdk_application_insights.types.workload_id


class RemoveWorkloadRequest(TypedDict, closed=True):
    resource_group_name: (
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: "aws_sdk_application_insights.types.component_name.ComponentName"
    """<p>The name of the component.</p>"""
    workload_id: "aws_sdk_application_insights.types.workload_id.WorkloadId"
    """<p>The ID of the workload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveWorkloadRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    out["WorkloadId"] = value["workload_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveWorkloadRequest:
    out: RemoveWorkloadRequest = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        raise DeserializationError("RemoveWorkloadRequest.resource_group_name required")
    if "ComponentName" in data:
        out["component_name"] = data["ComponentName"]
    else:
        raise DeserializationError("RemoveWorkloadRequest.component_name required")
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    else:
        raise DeserializationError("RemoveWorkloadRequest.workload_id required")
    return out
