"""Generated from Smithy shape ``com.amazonaws.omics#ListVariantStoresFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.store_status


class ListVariantStoresFilter(TypedDict, closed=True):
    status: NotRequired["capo_omics.types.store_status.StoreStatus"]
    """<p>A status to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVariantStoresFilter) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> ListVariantStoresFilter:
    out: ListVariantStoresFilter = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
