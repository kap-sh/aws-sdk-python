"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.last_resource_data_sync_message
    import capo_ssm.types.last_resource_data_sync_status
    import capo_ssm.types.last_resource_data_sync_time
    import capo_ssm.types.last_successful_resource_data_sync_time
    import capo_ssm.types.resource_data_sync_created_time
    import capo_ssm.types.resource_data_sync_last_modified_time
    import capo_ssm.types.resource_data_sync_name
    import capo_ssm.types.resource_data_sync_s3_destination
    import capo_ssm.types.resource_data_sync_source_with_state
    import capo_ssm.types.resource_data_sync_type


class ResourceDataSyncItem(TypedDict, closed=True):
    sync_name: NotRequired[
        "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    ]
    """<p>The name of the resource data sync.</p>"""
    sync_type: NotRequired[
        "capo_ssm.types.resource_data_sync_type.ResourceDataSyncType"
    ]
    """<p>The type of resource data sync. If <code>SyncType</code> is <code>SyncToDestination</code>, then the resource data sync synchronizes data to an S3 bucket. If the <code>SyncType</code> is <code>SyncFromSource</code> then the resource data sync synchronizes data from Organizations or from multiple Amazon Web Services Regions.</p>"""
    sync_source: NotRequired[
        "capo_ssm.types.resource_data_sync_source_with_state.ResourceDataSyncSourceWithState"
    ]
    """<p>Information about the source where the data was synchronized. </p>"""
    s3_destination: NotRequired[
        "capo_ssm.types.resource_data_sync_s3_destination.ResourceDataSyncS3Destination"
    ]
    """<p>Configuration information for the target S3 bucket.</p>"""
    last_sync_time: NotRequired[
        "capo_ssm.types.last_resource_data_sync_time.LastResourceDataSyncTime"
    ]
    """<p>The last time the configuration attempted to sync (UTC).</p>"""
    last_successful_sync_time: NotRequired[
        "capo_ssm.types.last_successful_resource_data_sync_time.LastSuccessfulResourceDataSyncTime"
    ]
    """<p>The last time the sync operations returned a status of <code>SUCCESSFUL</code> (UTC).</p>"""
    sync_last_modified_time: NotRequired[
        "capo_ssm.types.resource_data_sync_last_modified_time.ResourceDataSyncLastModifiedTime"
    ]
    """<p>The date and time the resource data sync was changed. </p>"""
    last_status: NotRequired[
        "capo_ssm.types.last_resource_data_sync_status.LastResourceDataSyncStatus"
    ]
    """<p>The status reported by the last sync.</p>"""
    sync_created_time: NotRequired[
        "capo_ssm.types.resource_data_sync_created_time.ResourceDataSyncCreatedTime"
    ]
    """<p>The date and time the configuration was created (UTC).</p>"""
    last_sync_status_message: NotRequired[
        "capo_ssm.types.last_resource_data_sync_message.LastResourceDataSyncMessage"
    ]
    """<p>The status message details reported by the last sync.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncItem) -> dict:
    out: dict = {}
    if "sync_name" in value:
        out["SyncName"] = value["sync_name"]
    if "sync_type" in value:
        out["SyncType"] = value["sync_type"]
    if "sync_source" in value:
        import capo_ssm.types.resource_data_sync_source_with_state

        out["SyncSource"] = (
            capo_ssm.types.resource_data_sync_source_with_state.serialize_aws_json_1_1(
                value["sync_source"]
            )
        )
    if "s3_destination" in value:
        import capo_ssm.types.resource_data_sync_s3_destination

        out["S3Destination"] = (
            capo_ssm.types.resource_data_sync_s3_destination.serialize_aws_json_1_1(
                value["s3_destination"]
            )
        )
    if "last_sync_time" in value:
        import capo_ssm.types.last_resource_data_sync_time

        out["LastSyncTime"] = (
            capo_ssm.types.last_resource_data_sync_time.serialize_aws_json_1_1(
                value["last_sync_time"]
            )
        )
    if "last_successful_sync_time" in value:
        import capo_ssm.types.last_successful_resource_data_sync_time

        out["LastSuccessfulSyncTime"] = (
            capo_ssm.types.last_successful_resource_data_sync_time.serialize_aws_json_1_1(
                value["last_successful_sync_time"]
            )
        )
    if "sync_last_modified_time" in value:
        import capo_ssm.types.resource_data_sync_last_modified_time

        out["SyncLastModifiedTime"] = (
            capo_ssm.types.resource_data_sync_last_modified_time.serialize_aws_json_1_1(
                value["sync_last_modified_time"]
            )
        )
    if "last_status" in value:
        import capo_ssm.types.last_resource_data_sync_status

        out["LastStatus"] = (
            capo_ssm.types.last_resource_data_sync_status.serialize_aws_json_1_1(
                value["last_status"]
            )
        )
    if "sync_created_time" in value:
        import capo_ssm.types.resource_data_sync_created_time

        out["SyncCreatedTime"] = (
            capo_ssm.types.resource_data_sync_created_time.serialize_aws_json_1_1(
                value["sync_created_time"]
            )
        )
    if "last_sync_status_message" in value:
        out["LastSyncStatusMessage"] = value["last_sync_status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDataSyncItem:
    out: ResourceDataSyncItem = {}  # type: ignore[typeddict-item]
    if "SyncName" in data:
        out["sync_name"] = data["SyncName"]
    if "SyncType" in data:
        out["sync_type"] = data["SyncType"]
    if "SyncSource" in data:
        import capo_ssm.types.resource_data_sync_source_with_state

        out["sync_source"] = (
            capo_ssm.types.resource_data_sync_source_with_state.deserialize_aws_json_1_1(
                data["SyncSource"]
            )
        )
    if "S3Destination" in data:
        import capo_ssm.types.resource_data_sync_s3_destination

        out["s3_destination"] = (
            capo_ssm.types.resource_data_sync_s3_destination.deserialize_aws_json_1_1(
                data["S3Destination"]
            )
        )
    if "LastSyncTime" in data:
        import capo_ssm.types.last_resource_data_sync_time

        out["last_sync_time"] = (
            capo_ssm.types.last_resource_data_sync_time.deserialize_aws_json_1_1(
                data["LastSyncTime"]
            )
        )
    if "LastSuccessfulSyncTime" in data:
        import capo_ssm.types.last_successful_resource_data_sync_time

        out["last_successful_sync_time"] = (
            capo_ssm.types.last_successful_resource_data_sync_time.deserialize_aws_json_1_1(
                data["LastSuccessfulSyncTime"]
            )
        )
    if "SyncLastModifiedTime" in data:
        import capo_ssm.types.resource_data_sync_last_modified_time

        out["sync_last_modified_time"] = (
            capo_ssm.types.resource_data_sync_last_modified_time.deserialize_aws_json_1_1(
                data["SyncLastModifiedTime"]
            )
        )
    if "LastStatus" in data:
        import capo_ssm.types.last_resource_data_sync_status

        out["last_status"] = (
            capo_ssm.types.last_resource_data_sync_status.deserialize_aws_json_1_1(
                data["LastStatus"]
            )
        )
    if "SyncCreatedTime" in data:
        import capo_ssm.types.resource_data_sync_created_time

        out["sync_created_time"] = (
            capo_ssm.types.resource_data_sync_created_time.deserialize_aws_json_1_1(
                data["SyncCreatedTime"]
            )
        )
    if "LastSyncStatusMessage" in data:
        out["last_sync_status_message"] = data["LastSyncStatusMessage"]
    return out
