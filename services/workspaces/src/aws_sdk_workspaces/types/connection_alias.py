"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAlias``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.aws_account
    import aws_sdk_workspaces.types.connection_alias_association_list
    import aws_sdk_workspaces.types.connection_alias_id
    import aws_sdk_workspaces.types.connection_alias_state
    import aws_sdk_workspaces.types.connection_string


class ConnectionAlias(TypedDict):
    connection_string: NotRequired[
        "aws_sdk_workspaces.types.connection_string.ConnectionString"
    ]
    """<p>The connection string specified for the connection alias. The connection string must be in the form of a fully qualified domain name (FQDN), such as <code>www.example.com</code>.</p>"""
    alias_id: NotRequired[
        "aws_sdk_workspaces.types.connection_alias_id.ConnectionAliasId"
    ]
    """<p>The identifier of the connection alias.</p>"""
    state: NotRequired[
        "aws_sdk_workspaces.types.connection_alias_state.ConnectionAliasState"
    ]
    """<p>The current state of the connection alias.</p>"""
    owner_account_id: NotRequired["aws_sdk_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the Amazon Web Services account that owns the connection alias.</p>"""
    associations: NotRequired[
        "aws_sdk_workspaces.types.connection_alias_association_list.ConnectionAliasAssociationList"
    ]
    """<p>The association status of the connection alias.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAlias) -> dict:
    out: dict = {}
    if "connection_string" in value:
        out["ConnectionString"] = value["connection_string"]
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "state" in value:
        import aws_sdk_workspaces.types.connection_alias_state

        out["State"] = (
            aws_sdk_workspaces.types.connection_alias_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "associations" in value:
        import aws_sdk_workspaces.types.connection_alias_association_list

        out["Associations"] = (
            aws_sdk_workspaces.types.connection_alias_association_list.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionAlias:
    out: ConnectionAlias = {}  # type: ignore[typeddict-item]
    if "ConnectionString" in data:
        out["connection_string"] = data["ConnectionString"]
    if "AliasId" in data:
        out["alias_id"] = data["AliasId"]
    if "State" in data:
        import aws_sdk_workspaces.types.connection_alias_state

        out["state"] = (
            aws_sdk_workspaces.types.connection_alias_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "Associations" in data:
        import aws_sdk_workspaces.types.connection_alias_association_list

        out["associations"] = (
            aws_sdk_workspaces.types.connection_alias_association_list.deserialize_aws_json_1_1(
                data["Associations"]
            )
        )
    return out
