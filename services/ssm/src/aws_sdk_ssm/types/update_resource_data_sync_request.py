"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateResourceDataSyncRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_data_sync_name
    import aws_sdk_ssm.types.resource_data_sync_source
    import aws_sdk_ssm.types.resource_data_sync_type


class UpdateResourceDataSyncRequest(TypedDict):
    sync_name: "aws_sdk_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    """<p>The name of the resource data sync you want to update.</p>"""
    sync_type: "aws_sdk_ssm.types.resource_data_sync_type.ResourceDataSyncType"
    """<p>The type of resource data sync. The supported <code>SyncType</code> is SyncFromSource.</p>"""
    sync_source: "aws_sdk_ssm.types.resource_data_sync_source.ResourceDataSyncSource"
    """<p>Specify information about the data sources to synchronize.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResourceDataSyncRequest) -> dict:
    out: dict = {}
    out["SyncName"] = value["sync_name"]
    out["SyncType"] = value["sync_type"]
    import aws_sdk_ssm.types.resource_data_sync_source

    out["SyncSource"] = (
        aws_sdk_ssm.types.resource_data_sync_source.serialize_aws_json_1_1(
            value["sync_source"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResourceDataSyncRequest:
    out: UpdateResourceDataSyncRequest = {}  # type: ignore[typeddict-item]
    if "SyncName" in data:
        out["sync_name"] = data["SyncName"]
    else:
        raise DeserializationError("UpdateResourceDataSyncRequest.sync_name required")
    if "SyncType" in data:
        out["sync_type"] = data["SyncType"]
    else:
        raise DeserializationError("UpdateResourceDataSyncRequest.sync_type required")
    if "SyncSource" in data:
        import aws_sdk_ssm.types.resource_data_sync_source

        out["sync_source"] = (
            aws_sdk_ssm.types.resource_data_sync_source.deserialize_aws_json_1_1(
                data["SyncSource"]
            )
        )
    else:
        raise DeserializationError("UpdateResourceDataSyncRequest.sync_source required")
    return out
