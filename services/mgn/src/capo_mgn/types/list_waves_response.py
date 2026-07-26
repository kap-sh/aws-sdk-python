"""Generated from Smithy shape ``com.amazonaws.mgn#ListWavesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.pagination_token
    import capo_mgn.types.waves_list


class ListWavesResponse(TypedDict, closed=True):
    items: NotRequired["capo_mgn.types.waves_list.WavesList"]
    """<p>Waves list.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>Response next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWavesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.waves_list

        out["items"] = capo_mgn.types.waves_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWavesResponse:
    out: ListWavesResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_mgn.types.waves_list

        out["items"] = capo_mgn.types.waves_list.deserialize_json(data["items"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
