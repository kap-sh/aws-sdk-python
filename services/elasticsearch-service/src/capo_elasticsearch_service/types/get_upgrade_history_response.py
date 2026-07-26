"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#GetUpgradeHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.string
    import capo_elasticsearch_service.types.upgrade_history_list


class GetUpgradeHistoryResponse(TypedDict, closed=True):
    upgrade_histories: NotRequired[
        "capo_elasticsearch_service.types.upgrade_history_list.UpgradeHistoryList"
    ]
    """<p> A list of <code> <a>UpgradeHistory</a> </code> objects corresponding to each Upgrade or Upgrade Eligibility Check performed on a domain returned as part of <code> <a>GetUpgradeHistoryResponse</a> </code> object. </p>"""
    next_token: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>Pagination token that needs to be supplied to the next call to get the next page of results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUpgradeHistoryResponse) -> dict:
    out: dict = {}
    if "upgrade_histories" in value:
        import capo_elasticsearch_service.types.upgrade_history_list

        out["UpgradeHistories"] = (
            capo_elasticsearch_service.types.upgrade_history_list.serialize_json(
                value["upgrade_histories"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetUpgradeHistoryResponse:
    out: GetUpgradeHistoryResponse = {}  # type: ignore[typeddict-item]
    if "UpgradeHistories" in data:
        import capo_elasticsearch_service.types.upgrade_history_list

        out["upgrade_histories"] = (
            capo_elasticsearch_service.types.upgrade_history_list.deserialize_json(
                data["UpgradeHistories"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
