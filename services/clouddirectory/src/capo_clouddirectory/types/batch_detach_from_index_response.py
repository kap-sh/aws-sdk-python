"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchDetachFromIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_identifier


class BatchDetachFromIndexResponse(TypedDict, closed=True):
    detached_object_identifier: NotRequired[
        "capo_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The <code>ObjectIdentifier</code> of the object that was detached from the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDetachFromIndexResponse) -> dict:
    out: dict = {}
    if "detached_object_identifier" in value:
        out["DetachedObjectIdentifier"] = value["detached_object_identifier"]
    return out


def deserialize_json(data: dict) -> BatchDetachFromIndexResponse:
    out: BatchDetachFromIndexResponse = {}  # type: ignore[typeddict-item]
    if "DetachedObjectIdentifier" in data:
        out["detached_object_identifier"] = data["DetachedObjectIdentifier"]
    return out
