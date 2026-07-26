"""Generated from Smithy shape ``com.amazonaws.codestarconnections#DeleteSyncConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_connections.types.resource_name
    import capo_codestar_connections.types.sync_configuration_type


class DeleteSyncConfigurationInput(TypedDict, closed=True):
    sync_type: (
        "capo_codestar_connections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The type of sync configuration to be deleted.</p>"""
    resource_name: "capo_codestar_connections.types.resource_name.ResourceName"
    """<p>The name of the Amazon Web Services resource associated with the sync configuration to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteSyncConfigurationInput) -> dict:
    out: dict = {}
    import capo_codestar_connections.types.sync_configuration_type

    out["SyncType"] = (
        capo_codestar_connections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    out["ResourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteSyncConfigurationInput:
    out: DeleteSyncConfigurationInput = {}  # type: ignore[typeddict-item]
    if "SyncType" in data:
        import capo_codestar_connections.types.sync_configuration_type

        out["sync_type"] = (
            capo_codestar_connections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        raise DeserializationError("DeleteSyncConfigurationInput.sync_type required")
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError(
            "DeleteSyncConfigurationInput.resource_name required"
        )
    return out
