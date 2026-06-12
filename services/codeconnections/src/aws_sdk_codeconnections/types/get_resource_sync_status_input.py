"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetResourceSyncStatusInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.resource_name
    import aws_sdk_codeconnections.types.sync_configuration_type


class GetResourceSyncStatusInput(TypedDict):
    resource_name: "aws_sdk_codeconnections.types.resource_name.ResourceName"
    """<p>The name of the Amazon Web Services resource for the sync status with the Git repository.</p>"""
    sync_type: (
        "aws_sdk_codeconnections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The sync type for the sync status with the Git repository.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceSyncStatusInput) -> dict:
    out: dict = {}
    out["ResourceName"] = value["resource_name"]
    import aws_sdk_codeconnections.types.sync_configuration_type

    out["SyncType"] = (
        aws_sdk_codeconnections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceSyncStatusInput:
    out: GetResourceSyncStatusInput = {}  # type: ignore[typeddict-item]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError("GetResourceSyncStatusInput.resource_name required")
    if "SyncType" in data:
        import aws_sdk_codeconnections.types.sync_configuration_type

        out["sync_type"] = (
            aws_sdk_codeconnections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        raise DeserializationError("GetResourceSyncStatusInput.sync_type required")
    return out
