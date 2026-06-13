"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceInstanceSyncStatusInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name


class GetServiceInstanceSyncStatusInput(TypedDict):
    service_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service that the service instance belongs to.</p>"""
    service_instance_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service instance that you want the sync status input for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceInstanceSyncStatusInput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    out["serviceInstanceName"] = value["service_instance_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceInstanceSyncStatusInput:
    out: GetServiceInstanceSyncStatusInput = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError(
            "GetServiceInstanceSyncStatusInput.service_name required"
        )
    if "serviceInstanceName" in data:
        out["service_instance_name"] = data["serviceInstanceName"]
    else:
        raise DeserializationError(
            "GetServiceInstanceSyncStatusInput.service_instance_name required"
        )
    return out
