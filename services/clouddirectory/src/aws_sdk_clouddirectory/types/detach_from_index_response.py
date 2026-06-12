"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DetachFromIndexResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_identifier


class DetachFromIndexResponse(TypedDict):
    detached_object_identifier: NotRequired[
        "aws_sdk_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The <code>ObjectIdentifier</code> of the object that was detached from the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetachFromIndexResponse) -> dict:
    out: dict = {}
    if "detached_object_identifier" in value:
        out["DetachedObjectIdentifier"] = value["detached_object_identifier"]
    return out


def deserialize_json(data: dict) -> DetachFromIndexResponse:
    out: DetachFromIndexResponse = {}  # type: ignore[typeddict-item]
    if "DetachedObjectIdentifier" in data:
        out["detached_object_identifier"] = data["DetachedObjectIdentifier"]
    return out
