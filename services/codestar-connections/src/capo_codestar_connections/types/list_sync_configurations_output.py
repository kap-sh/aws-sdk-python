"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ListSyncConfigurationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codestar_connections.types.sharp_next_token
    import capo_codestar_connections.types.sync_configuration_list


class ListSyncConfigurationsOutput(TypedDict, closed=True):
    sync_configurations: (
        "capo_codestar_connections.types.sync_configuration_list.SyncConfigurationList"
    )
    """<p>The list of repository sync definitions returned by the request.</p>"""
    next_token: NotRequired[
        "capo_codestar_connections.types.sharp_next_token.SharpNextToken"
    ]
    """<p>An enumeration token that allows the operation to batch the next results of the operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSyncConfigurationsOutput) -> dict:
    out: dict = {}
    import capo_codestar_connections.types.sync_configuration_list

    out["SyncConfigurations"] = (
        capo_codestar_connections.types.sync_configuration_list.serialize_aws_json_1_0(
            value["sync_configurations"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSyncConfigurationsOutput:
    out: ListSyncConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if "SyncConfigurations" in data:
        import capo_codestar_connections.types.sync_configuration_list

        out["sync_configurations"] = (
            capo_codestar_connections.types.sync_configuration_list.deserialize_aws_json_1_0(
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
