"""Generated from Smithy shape ``com.amazonaws.codestarconnections#CreateSyncConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.sync_configuration


class CreateSyncConfigurationOutput(TypedDict):
    sync_configuration: (
        "aws_sdk_codestar_connections.types.sync_configuration.SyncConfiguration"
    )
    """<p>The created sync configuration for the connection. A sync configuration allows Amazon Web Services to sync content from a Git repository to update a specified Amazon Web Services resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateSyncConfigurationOutput) -> dict:
    out: dict = {}
    import aws_sdk_codestar_connections.types.sync_configuration

    out["SyncConfiguration"] = (
        aws_sdk_codestar_connections.types.sync_configuration.serialize_aws_json_1_0(
            value["sync_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateSyncConfigurationOutput:
    out: CreateSyncConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "SyncConfiguration" in data:
        import aws_sdk_codestar_connections.types.sync_configuration

        out["sync_configuration"] = (
            aws_sdk_codestar_connections.types.sync_configuration.deserialize_aws_json_1_0(
                data["SyncConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSyncConfigurationOutput.sync_configuration required"
        )
    return out
