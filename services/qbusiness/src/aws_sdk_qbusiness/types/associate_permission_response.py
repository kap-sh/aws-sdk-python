"""Generated from Smithy shape ``com.amazonaws.qbusiness#AssociatePermissionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.string

class AssociatePermissionResponse(TypedDict):
    statement: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The JSON representation of the added permission statement.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssociatePermissionResponse) -> dict:
    out: dict = {}
    if "statement" in value:
        out["statement"] = value["statement"]
    return out


def deserialize_json(data: dict) -> AssociatePermissionResponse:
    out: AssociatePermissionResponse = {}  # type: ignore[typeddict-item]
    if "statement" in data:
        out["statement"] = data["statement"]
    return out