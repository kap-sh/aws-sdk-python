"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttachToIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_identifier


class AttachToIndexResponse(TypedDict, closed=True):
    attached_object_identifier: NotRequired[
        "capo_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The <code>ObjectIdentifier</code> of the object that was attached to the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachToIndexResponse) -> dict:
    out: dict = {}
    if "attached_object_identifier" in value:
        out["AttachedObjectIdentifier"] = value["attached_object_identifier"]
    return out


def deserialize_json(data: dict) -> AttachToIndexResponse:
    out: AttachToIndexResponse = {}  # type: ignore[typeddict-item]
    if "AttachedObjectIdentifier" in data:
        out["attached_object_identifier"] = data["AttachedObjectIdentifier"]
    return out
