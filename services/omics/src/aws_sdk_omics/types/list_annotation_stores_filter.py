"""Generated from Smithy shape ``com.amazonaws.omics#ListAnnotationStoresFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.store_status


class ListAnnotationStoresFilter(TypedDict):
    status: NotRequired["aws_sdk_omics.types.store_status.StoreStatus"]
    """<p>A status to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnnotationStoresFilter) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> ListAnnotationStoresFilter:
    out: ListAnnotationStoresFilter = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
