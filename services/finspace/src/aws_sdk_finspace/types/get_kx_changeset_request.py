"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxChangesetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.changeset_id
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.environment_id


class GetKxChangesetRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    database_name: "aws_sdk_finspace.types.database_name.DatabaseName"
    """<p>The name of the kdb database.</p>"""
    changeset_id: "aws_sdk_finspace.types.changeset_id.ChangesetId"
    """<p>A unique identifier of the changeset for which you want to retrieve data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxChangesetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKxChangesetRequest:
    out: GetKxChangesetRequest = {}  # type: ignore[typeddict-item]
    return out
