"""Generated from Smithy shape ``com.amazonaws.lambda#AddLayerVersionPermissionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class AddLayerVersionPermissionResponse(TypedDict):
    statement: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The permission statement.</p>"""
    revision_id: NotRequired["aws_sdk_lambda.types.string.String"]
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
    if "Statement" in data:
        out["statement"] = data["Statement"]
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    return out
