"""Generated from Smithy shape ``com.amazonaws.dataexchange#GetAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.id


class GetAssetRequest(TypedDict, closed=True):
    asset_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for an asset.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for a data set.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for a revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssetRequest:
    out: GetAssetRequest = {}  # type: ignore[typeddict-item]
    return out
