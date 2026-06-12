"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociateConnectionAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.connection_alias_id
    import aws_sdk_workspaces.types.non_empty_string


class AssociateConnectionAliasRequest(TypedDict):
    alias_id: "aws_sdk_workspaces.types.connection_alias_id.ConnectionAliasId"
    """<p>The identifier of the connection alias.</p>"""
    resource_id: "aws_sdk_workspaces.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the directory to associate the connection alias with.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateConnectionAliasRequest) -> dict:
    out: dict = {}
    out["AliasId"] = value["alias_id"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateConnectionAliasRequest:
    out: AssociateConnectionAliasRequest = {}  # type: ignore[typeddict-item]
    if "AliasId" in data:
        out["alias_id"] = data["AliasId"]
    else:
        raise DeserializationError("AssociateConnectionAliasRequest.alias_id required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "AssociateConnectionAliasRequest.resource_id required"
        )
    return out
