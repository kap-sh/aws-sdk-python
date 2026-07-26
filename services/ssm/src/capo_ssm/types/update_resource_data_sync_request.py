"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateResourceDataSyncRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.resource_data_sync_name
    import capo_ssm.types.resource_data_sync_source
    import capo_ssm.types.resource_data_sync_type


class UpdateResourceDataSyncRequest(TypedDict, closed=True):
    sync_name: "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    """<p>The name of the resource data sync you want to update.</p>"""
    sync_type: "capo_ssm.types.resource_data_sync_type.ResourceDataSyncType"
    """<p>The type of resource data sync. The supported <code>SyncType</code> is SyncFromSource.</p>"""
    sync_source: "capo_ssm.types.resource_data_sync_source.ResourceDataSyncSource"
    """<p>Specify information about the data sources to synchronize.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResourceDataSyncRequest) -> dict:
    out: dict = {}
    out["SyncName"] = value["sync_name"]
    out["SyncType"] = value["sync_type"]
    import capo_ssm.types.resource_data_sync_source

    out["SyncSource"] = capo_ssm.types.resource_data_sync_source.serialize_aws_json_1_1(
        value["sync_source"]
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
        import capo_ssm.types.resource_data_sync_source

        out["sync_source"] = (
            capo_ssm.types.resource_data_sync_source.deserialize_aws_json_1_1(
                data["SyncSource"]
            )
        )
    else:
        raise DeserializationError("UpdateResourceDataSyncRequest.sync_source required")
    return out
