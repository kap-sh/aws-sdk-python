"""Generated from Smithy shape ``com.amazonaws.kendra#ListDataSourceSyncJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_sync_job_history_list
    import capo_kendra.types.next_token


class ListDataSourceSyncJobsResponse(TypedDict, closed=True):
    history: NotRequired[
        "capo_kendra.types.data_source_sync_job_history_list.DataSourceSyncJobHistoryList"
    ]
    """<p>A history of synchronization jobs for the data source connector.</p>"""
    next_token: NotRequired["capo_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of jobs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataSourceSyncJobsResponse) -> dict:
    out: dict = {}
    if "history" in value:
        import capo_kendra.types.data_source_sync_job_history_list

        out["History"] = (
            capo_kendra.types.data_source_sync_job_history_list.serialize_aws_json_1_1(
                value["history"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataSourceSyncJobsResponse:
    out: ListDataSourceSyncJobsResponse = {}  # type: ignore[typeddict-item]
    if "History" in data:
        import capo_kendra.types.data_source_sync_job_history_list

        out["history"] = (
            capo_kendra.types.data_source_sync_job_history_list.deserialize_aws_json_1_1(
                data["History"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
