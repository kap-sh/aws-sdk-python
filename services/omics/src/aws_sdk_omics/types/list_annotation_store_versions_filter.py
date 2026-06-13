"""Generated from Smithy shape ``com.amazonaws.omics#ListAnnotationStoreVersionsFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.version_status


class ListAnnotationStoreVersionsFilter(TypedDict):
    status: NotRequired["aws_sdk_omics.types.version_status.VersionStatus"]
    """<p>The status of an annotation store version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnnotationStoreVersionsFilter) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> ListAnnotationStoreVersionsFilter:
    out: ListAnnotationStoreVersionsFilter = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
