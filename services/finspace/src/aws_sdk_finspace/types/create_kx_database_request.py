"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxDatabaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token_string
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.environment_id
    import aws_sdk_finspace.types.tag_map


class CreateKxDatabaseRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    database_name: "aws_sdk_finspace.types.database_name.DatabaseName"
    """<p>The name of the kdb database.</p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p>A description of the database.</p>"""
    tags: NotRequired["aws_sdk_finspace.types.tag_map.TagMap"]
    """<p>A list of key-value pairs to label the kdb database. You can add up to 50 tags to your kdb database</p>"""
    client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString"
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxDatabaseRequest) -> dict:
    out: dict = {}
    out["databaseName"] = value["database_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_finspace.types.tag_map

        out["tags"] = aws_sdk_finspace.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateKxDatabaseRequest:
    out: CreateKxDatabaseRequest = {}  # type: ignore[typeddict-item]
    if "databaseName" in data:
        out["database_name"] = data["databaseName"]
    else:
        raise DeserializationError("CreateKxDatabaseRequest.database_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_finspace.types.tag_map

        out["tags"] = aws_sdk_finspace.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateKxDatabaseRequest.client_token required")
    return out
