"""Generated from Smithy shape ``com.amazonaws.connect#ListApprovedOriginsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.origins_list


class ListApprovedOriginsResponse(TypedDict, closed=True):
    origins: NotRequired["capo_connect.types.origins_list.OriginsList"]
    """<p>The approved origins.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApprovedOriginsResponse) -> dict:
    out: dict = {}
    if "origins" in value:
        import capo_connect.types.origins_list

        out["Origins"] = capo_connect.types.origins_list.serialize_json(
            value["origins"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApprovedOriginsResponse:
    out: ListApprovedOriginsResponse = {}  # type: ignore[typeddict-item]
    if "Origins" in data:
        import capo_connect.types.origins_list

        out["origins"] = capo_connect.types.origins_list.deserialize_json(
            data["Origins"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
