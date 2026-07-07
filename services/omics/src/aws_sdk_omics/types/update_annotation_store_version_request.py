"""Generated from Smithy shape ``com.amazonaws.omics#UpdateAnnotationStoreVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.description


class UpdateAnnotationStoreVersionRequest(TypedDict, closed=True):
    name: "str"
    """<p> The name of an annotation store. </p>"""
    version_name: "str"
    """<p> The name of an annotation store version. </p>"""
    description: NotRequired["aws_sdk_omics.types.description.Description"]
    """<p> The description of an annotation store. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnnotationStoreVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateAnnotationStoreVersionRequest:
    out: UpdateAnnotationStoreVersionRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
