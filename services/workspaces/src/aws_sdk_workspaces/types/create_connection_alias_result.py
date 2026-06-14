"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateConnectionAliasResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.connection_alias_id


class CreateConnectionAliasResult(TypedDict):
    alias_id: NotRequired[
        "aws_sdk_workspaces.types.connection_alias_id.ConnectionAliasId"
    ]
    """<p>The identifier of the connection alias.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionAliasResult) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionAliasResult:
    out: CreateConnectionAliasResult = {}  # type: ignore[typeddict-item]
    if "AliasId" in data:
        out["alias_id"] = data["AliasId"]
    return out
