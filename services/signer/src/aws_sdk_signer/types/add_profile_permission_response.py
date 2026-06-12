"""Generated from Smithy shape ``com.amazonaws.signer#AddProfilePermissionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signer.types.string


class AddProfilePermissionResponse(TypedDict):
    revision_id: NotRequired["aws_sdk_signer.types.string.String"]
    """<p>A unique identifier for the current profile revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddProfilePermissionResponse) -> dict:
    out: dict = {}
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> AddProfilePermissionResponse:
    out: AddProfilePermissionResponse = {}  # type: ignore[typeddict-item]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    return out
