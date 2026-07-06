"""Generated from Smithy shape ``com.amazonaws.omics#UpdateAnnotationStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.description


class UpdateAnnotationStoreRequest(TypedDict, closed=True):
    name: "str"
    """<p>A name for the store.</p>"""
    description: NotRequired["aws_sdk_omics.types.description.Description"]
    """<p>A description for the store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnnotationStoreRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateAnnotationStoreRequest:
    out: UpdateAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
