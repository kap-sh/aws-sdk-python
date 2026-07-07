"""Generated from Smithy shape ``com.amazonaws.finspace#DeleteKxDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token_string
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.environment_id


class DeleteKxDatabaseRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    database_name: "aws_sdk_finspace.types.database_name.DatabaseName"
    """<p>The name of the kdb database that you want to delete.</p>"""
    client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString"
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKxDatabaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKxDatabaseRequest:
    out: DeleteKxDatabaseRequest = {}  # type: ignore[typeddict-item]
    return out
