"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateConnectionAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.connection_string
    import aws_sdk_workspaces.types.tag_list


class CreateConnectionAliasRequest(TypedDict):
    connection_string: "aws_sdk_workspaces.types.connection_string.ConnectionString"
    """<p>A connection string in the form of a fully qualified domain name (FQDN), such as <code>www.example.com</code>.</p> <important> <p>After you create a connection string, it is always associated to your Amazon Web Services account. You cannot recreate the same connection string with a different account, even if you delete all instances of it from the original account. The connection string is globally reserved for your account.</p> </important>"""
    tags: NotRequired["aws_sdk_workspaces.types.tag_list.TagList"]
    """<p>The tags to associate with the connection alias.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionAliasRequest) -> dict:
    out: dict = {}
    out["ConnectionString"] = value["connection_string"]
    if "tags" in value:
        import aws_sdk_workspaces.types.tag_list

        out["Tags"] = aws_sdk_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionAliasRequest:
    out: CreateConnectionAliasRequest = {}  # type: ignore[typeddict-item]
    if "ConnectionString" in data:
        out["connection_string"] = data["ConnectionString"]
    else:
        raise DeserializationError(
            "CreateConnectionAliasRequest.connection_string required"
        )
    if "Tags" in data:
        import aws_sdk_workspaces.types.tag_list

        out["tags"] = aws_sdk_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
