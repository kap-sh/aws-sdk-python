"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token_string
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.environment_id


class UpdateKxDatabaseRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    database_name: "aws_sdk_finspace.types.database_name.DatabaseName"
    """<p>The name of the kdb database.</p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p>A description of the database.</p>"""
    client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString"
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxDatabaseRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateKxDatabaseRequest:
    out: UpdateKxDatabaseRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("UpdateKxDatabaseRequest.client_token required")
    return out
