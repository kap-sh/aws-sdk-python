"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectionAliasPermission``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.aws_account
    import aws_sdk_workspaces.types.boolean_object


class ConnectionAliasPermission(TypedDict, closed=True):
    shared_account_id: "aws_sdk_workspaces.types.aws_account.AwsAccount"
    """<p>The identifier of the Amazon Web Services account that the connection alias is shared with.</p>"""
    allow_association: "aws_sdk_workspaces.types.boolean_object.BooleanObject"
    """<p>Indicates whether the specified Amazon Web Services account is allowed to associate the connection alias with a directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAliasPermission) -> dict:
    out: dict = {}
    out["SharedAccountId"] = value["shared_account_id"]
    out["AllowAssociation"] = value["allow_association"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionAliasPermission:
    out: ConnectionAliasPermission = {}  # type: ignore[typeddict-item]
    if "SharedAccountId" in data:
        out["shared_account_id"] = data["SharedAccountId"]
    else:
        raise DeserializationError(
            "ConnectionAliasPermission.shared_account_id required"
        )
    if "AllowAssociation" in data:
        out["allow_association"] = data["AllowAssociation"]
    else:
        raise DeserializationError(
            "ConnectionAliasPermission.allow_association required"
        )
    return out
