"""Generated from Smithy shape ``com.amazonaws.ssm#DeleteResourceDataSyncRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_data_sync_name
    import aws_sdk_ssm.types.resource_data_sync_type


class DeleteResourceDataSyncRequest(TypedDict):
    sync_name: "aws_sdk_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    """<p>The name of the configuration to delete.</p>"""
    sync_type: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_type.ResourceDataSyncType"
    ]
    """<p>Specify the type of resource data sync to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResourceDataSyncRequest) -> dict:
    out: dict = {}
    out["SyncName"] = value["sync_name"]
    if "sync_type" in value:
        out["SyncType"] = value["sync_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResourceDataSyncRequest:
    out: DeleteResourceDataSyncRequest = {}  # type: ignore[typeddict-item]
    if "SyncName" in data:
        out["sync_name"] = data["SyncName"]
    else:
        raise DeserializationError("DeleteResourceDataSyncRequest.sync_name required")
    if "SyncType" in data:
        out["sync_type"] = data["SyncType"]
    return out
