"""Generated from Smithy shape ``com.amazonaws.lambda#AddLayerVersionPermissionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.string


class AddLayerVersionPermissionResponse(TypedDict, closed=True):
    statement: NotRequired["capo_lambda.types.string.String"]
    """<p>The permission statement.</p>"""
    revision_id: NotRequired["capo_lambda.types.string.String"]
    """<p>A unique identifier for the current revision of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddLayerVersionPermissionResponse) -> dict:
    out: dict = {}
    if "statement" in value:
        out["Statement"] = value["statement"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> AddLayerVersionPermissionResponse:
    out: AddLayerVersionPermissionResponse = {}  # type: ignore[typeddict-item]
    if data.get("Statement") is not None:
        out["statement"] = data["Statement"]
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    return out
