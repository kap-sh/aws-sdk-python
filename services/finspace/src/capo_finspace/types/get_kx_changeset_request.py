"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxChangesetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.changeset_id
    import capo_finspace.types.database_name
    import capo_finspace.types.environment_id


class GetKxChangesetRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    database_name: "capo_finspace.types.database_name.DatabaseName"
    """<p>The name of the kdb database.</p>"""
    changeset_id: "capo_finspace.types.changeset_id.ChangesetId"
    """<p>A unique identifier of the changeset for which you want to retrieve data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxChangesetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKxChangesetRequest:
    out: GetKxChangesetRequest = {}  # type: ignore[typeddict-item]
    return out
