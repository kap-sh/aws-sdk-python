"""Generated from Smithy shape ``com.amazonaws.codestarconnections#UpdateSyncConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.sync_configuration


class UpdateSyncConfigurationOutput(TypedDict, closed=True):
    sync_configuration: (
        "aws_sdk_codestar_connections.types.sync_configuration.SyncConfiguration"
    )
    """<p>The information returned for the sync configuration to be updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSyncConfigurationOutput) -> dict:
    out: dict = {}
    import aws_sdk_codestar_connections.types.sync_configuration

    out["SyncConfiguration"] = (
        aws_sdk_codestar_connections.types.sync_configuration.serialize_aws_json_1_0(
            value["sync_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSyncConfigurationOutput:
    out: UpdateSyncConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "SyncConfiguration" in data:
        import aws_sdk_codestar_connections.types.sync_configuration

        out["sync_configuration"] = (
            aws_sdk_codestar_connections.types.sync_configuration.deserialize_aws_json_1_0(
                data["SyncConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSyncConfigurationOutput.sync_configuration required"
        )
    return out
