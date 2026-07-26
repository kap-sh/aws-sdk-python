"""Generated from Smithy shape ``com.amazonaws.opensearch#GetUpgradeHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.string
    import capo_opensearch.types.upgrade_history_list


class GetUpgradeHistoryResponse(TypedDict, closed=True):
    upgrade_histories: NotRequired[
        "capo_opensearch.types.upgrade_history_list.UpgradeHistoryList"
    ]
    """<p>A list of objects corresponding to each upgrade or upgrade eligibility check performed on a domain.</p>"""
    next_token: NotRequired["capo_opensearch.types.string.String"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUpgradeHistoryResponse) -> dict:
    out: dict = {}
    if "upgrade_histories" in value:
        import capo_opensearch.types.upgrade_history_list

        out["UpgradeHistories"] = (
            capo_opensearch.types.upgrade_history_list.serialize_json(
                value["upgrade_histories"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetUpgradeHistoryResponse:
    out: GetUpgradeHistoryResponse = {}  # type: ignore[typeddict-item]
    if "UpgradeHistories" in data:
        import capo_opensearch.types.upgrade_history_list

        out["upgrade_histories"] = (
            capo_opensearch.types.upgrade_history_list.deserialize_json(
                data["UpgradeHistories"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
