"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListRevisionAssetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.list_of_asset_entry
    import capo_dataexchange.types.next_token


class ListRevisionAssetsResponse(TypedDict, closed=True):
    assets: NotRequired["capo_dataexchange.types.list_of_asset_entry.ListOfAssetEntry"]
    """<p>The asset objects listed by the request.</p>"""
    next_token: NotRequired["capo_dataexchange.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRevisionAssetsResponse) -> dict:
    out: dict = {}
    if "assets" in value:
        import capo_dataexchange.types.list_of_asset_entry

        out["Assets"] = capo_dataexchange.types.list_of_asset_entry.serialize_json(
            value["assets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRevisionAssetsResponse:
    out: ListRevisionAssetsResponse = {}  # type: ignore[typeddict-item]
    if "Assets" in data:
        import capo_dataexchange.types.list_of_asset_entry

        out["assets"] = capo_dataexchange.types.list_of_asset_entry.deserialize_json(
            data["Assets"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
