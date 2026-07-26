"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchDetachObjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_identifier


class BatchDetachObjectResponse(TypedDict, closed=True):
    detached_object_identifier: NotRequired[
        "capo_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The <code>ObjectIdentifier</code> of the detached object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDetachObjectResponse) -> dict:
    out: dict = {}
    if "detached_object_identifier" in value:
        out["detachedObjectIdentifier"] = value["detached_object_identifier"]
    return out


def deserialize_json(data: dict) -> BatchDetachObjectResponse:
    out: BatchDetachObjectResponse = {}  # type: ignore[typeddict-item]
    if "detachedObjectIdentifier" in data:
        out["detached_object_identifier"] = data["detachedObjectIdentifier"]
    return out
