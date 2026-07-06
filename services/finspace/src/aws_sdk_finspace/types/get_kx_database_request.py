"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.environment_id


class GetKxDatabaseRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    database_name: "aws_sdk_finspace.types.database_name.DatabaseName"
    """<p>The name of the kdb database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxDatabaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKxDatabaseRequest:
    out: GetKxDatabaseRequest = {}  # type: ignore[typeddict-item]
    return out
