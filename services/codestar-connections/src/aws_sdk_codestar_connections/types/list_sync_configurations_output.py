"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ListSyncConfigurationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.sharp_next_token
    import aws_sdk_codestar_connections.types.sync_configuration_list


class ListSyncConfigurationsOutput(TypedDict):
    sync_configurations: "aws_sdk_codestar_connections.types.sync_configuration_list.SyncConfigurationList"
    """<p>The list of repository sync definitions returned by the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_codestar_connections.types.sharp_next_token.SharpNextToken"
    ]
    """<p>An enumeration token that allows the operation to batch the next results of the operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSyncConfigurationsOutput) -> dict:
    out: dict = {}
    import aws_sdk_codestar_connections.types.sync_configuration_list

    out["SyncConfigurations"] = (
        aws_sdk_codestar_connections.types.sync_configuration_list.serialize_aws_json_1_0(
            value["sync_configurations"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSyncConfigurationsOutput:
    out: ListSyncConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if "SyncConfigurations" in data:
        import aws_sdk_codestar_connections.types.sync_configuration_list

        out["sync_configurations"] = (
            aws_sdk_codestar_connections.types.sync_configuration_list.deserialize_aws_json_1_0(
                data["SyncConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "ListSyncConfigurationsOutput.sync_configurations required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
