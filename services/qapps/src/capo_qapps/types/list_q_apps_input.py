"""Generated from Smithy shape ``com.amazonaws.qapps#ListQAppsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.instance_id
    import capo_qapps.types.page_limit
    import capo_qapps.types.pagination_token


class ListQAppsInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    limit: NotRequired["capo_qapps.types.page_limit.PageLimit"]
    """<p>The maximum number of Q Apps to return in the response.</p>"""
    next_token: NotRequired["capo_qapps.types.pagination_token.PaginationToken"]
    """<p>The token to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQAppsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQAppsInput:
    out: ListQAppsInput = {}  # type: ignore[typeddict-item]
    return out
