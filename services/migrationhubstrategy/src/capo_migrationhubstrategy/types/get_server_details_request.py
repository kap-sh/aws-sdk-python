"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetServerDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.max_result
    import capo_migrationhubstrategy.types.next_token
    import capo_migrationhubstrategy.types.server_id


class GetServerDetailsRequest(TypedDict, closed=True):
    server_id: "capo_migrationhubstrategy.types.server_id.ServerId"
    """<p> The ID of the server. </p>"""
    next_token: NotRequired["capo_migrationhubstrategy.types.next_token.NextToken"]
    """<p> The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. </p>"""
    max_results: NotRequired["capo_migrationhubstrategy.types.max_result.MaxResult"]
    """<p> The maximum number of items to include in the response. The maximum value is 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServerDetailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServerDetailsRequest:
    out: GetServerDetailsRequest = {}  # type: ignore[typeddict-item]
    return out
