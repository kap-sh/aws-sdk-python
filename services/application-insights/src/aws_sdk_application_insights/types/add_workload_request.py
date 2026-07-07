"""Generated from Smithy shape ``com.amazonaws.applicationinsights#AddWorkloadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_insights.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.component_name
    import aws_sdk_application_insights.types.resource_group_name
    import aws_sdk_application_insights.types.workload_configuration


class AddWorkloadRequest(TypedDict, closed=True):
    resource_group_name: (
        "aws_sdk_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: "aws_sdk_application_insights.types.component_name.ComponentName"
    """<p>The name of the component.</p>"""
    workload_configuration: "aws_sdk_application_insights.types.workload_configuration.WorkloadConfiguration"
    """<p>The configuration settings of the workload. The value is the escaped JSON of the configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddWorkloadRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    import aws_sdk_application_insights.types.workload_configuration

    out["WorkloadConfiguration"] = (
        aws_sdk_application_insights.types.workload_configuration.serialize_aws_json_1_1(
            value["workload_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddWorkloadRequest:
    out: AddWorkloadRequest = {}  # type: ignore[typeddict-item]
    if "ResourceGroupName" in data:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        raise DeserializationError("AddWorkloadRequest.resource_group_name required")
    if "ComponentName" in data:
        out["component_name"] = data["ComponentName"]
    else:
        raise DeserializationError("AddWorkloadRequest.component_name required")
    if "WorkloadConfiguration" in data:
        import aws_sdk_application_insights.types.workload_configuration

        out["workload_configuration"] = (
            aws_sdk_application_insights.types.workload_configuration.deserialize_aws_json_1_1(
                data["WorkloadConfiguration"]
            )
        )
    else:
        raise DeserializationError("AddWorkloadRequest.workload_configuration required")
    return out
