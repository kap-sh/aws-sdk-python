"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchAttachObjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_identifier


class BatchAttachObjectResponse(TypedDict, closed=True):
    attached_object_identifier: NotRequired[
        "capo_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The <code>ObjectIdentifier</code> of the object that has been attached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAttachObjectResponse) -> dict:
    out: dict = {}
    if "attached_object_identifier" in value:
        out["attachedObjectIdentifier"] = value["attached_object_identifier"]
    return out


def deserialize_json(data: dict) -> BatchAttachObjectResponse:
    out: BatchAttachObjectResponse = {}  # type: ignore[typeddict-item]
    if "attachedObjectIdentifier" in data:
        out["attached_object_identifier"] = data["attachedObjectIdentifier"]
    return out
