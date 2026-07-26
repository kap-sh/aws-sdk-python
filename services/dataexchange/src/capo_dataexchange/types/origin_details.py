"""Generated from Smithy shape ``com.amazonaws.dataexchange#OriginDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string


class OriginDetails(TypedDict, closed=True):
    product_id: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The product ID of the origin of the data set.</p>"""
    data_grant_id: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The ID of the data grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OriginDetails) -> dict:
    out: dict = {}
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "data_grant_id" in value:
        out["DataGrantId"] = value["data_grant_id"]
    return out


def deserialize_json(data: dict) -> OriginDetails:
    out: OriginDetails = {}  # type: ignore[typeddict-item]
    if "ProductId" in data:
        out["product_id"] = data["ProductId"]
    if "DataGrantId" in data:
        out["data_grant_id"] = data["DataGrantId"]
    return out
