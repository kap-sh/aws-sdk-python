"""Generated from Smithy shape ``com.amazonaws.securityhub#GetFindingHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.finding_history_record_list
    import capo_securityhub.types.next_token


class GetFindingHistoryResponse(TypedDict, closed=True):
    records: NotRequired[
        "capo_securityhub.types.finding_history_record_list.FindingHistoryRecordList"
    ]
    """<p> A list of events that altered the specified finding during the specified time period. </p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p> A token for pagination purposes. Provide this token in the subsequent request to <code>GetFindingsHistory</code> to get up to an additional 100 results of history for the same finding that you specified in your initial request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingHistoryResponse) -> dict:
    out: dict = {}
    if "records" in value:
        import capo_securityhub.types.finding_history_record_list

        out["Records"] = (
            capo_securityhub.types.finding_history_record_list.serialize_json(
                value["records"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetFindingHistoryResponse:
    out: GetFindingHistoryResponse = {}  # type: ignore[typeddict-item]
    if "Records" in data:
        import capo_securityhub.types.finding_history_record_list

        out["records"] = (
            capo_securityhub.types.finding_history_record_list.deserialize_json(
                data["Records"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
