"""Generated from Smithy shape ``com.amazonaws.codestarconnections#GetSyncConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.resource_name
    import aws_sdk_codestar_connections.types.sync_configuration_type


class GetSyncConfigurationInput(TypedDict, closed=True):
    sync_type: "aws_sdk_codestar_connections.types.sync_configuration_type.SyncConfigurationType"
    """<p>The sync type for the sync configuration for which you want to retrieve information.</p>"""
    resource_name: "aws_sdk_codestar_connections.types.resource_name.ResourceName"
    """<p>The name of the Amazon Web Services resource for the sync configuration for which you want to retrieve information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSyncConfigurationInput) -> dict:
    out: dict = {}
    import aws_sdk_codestar_connections.types.sync_configuration_type

    out["SyncType"] = (
        aws_sdk_codestar_connections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    out["ResourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSyncConfigurationInput:
    out: GetSyncConfigurationInput = {}  # type: ignore[typeddict-item]
    if "SyncType" in data:
        import aws_sdk_codestar_connections.types.sync_configuration_type

        out["sync_type"] = (
            aws_sdk_codestar_connections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        raise DeserializationError("GetSyncConfigurationInput.sync_type required")
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError("GetSyncConfigurationInput.resource_name required")
    return out
