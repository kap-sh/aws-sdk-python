"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchUpdateObjectAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_identifier


class BatchUpdateObjectAttributesResponse(TypedDict, closed=True):
    object_identifier: NotRequired[
        "capo_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>ID that is associated with the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateObjectAttributesResponse) -> dict:
    out: dict = {}
    if "object_identifier" in value:
        out["ObjectIdentifier"] = value["object_identifier"]
    return out


def deserialize_json(data: dict) -> BatchUpdateObjectAttributesResponse:
    out: BatchUpdateObjectAttributesResponse = {}  # type: ignore[typeddict-item]
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    return out
