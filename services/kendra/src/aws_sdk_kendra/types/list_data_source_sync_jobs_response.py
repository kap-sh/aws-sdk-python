"""Generated from Smithy shape ``com.amazonaws.kendra#ListDataSourceSyncJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.data_source_sync_job_history_list
    import aws_sdk_kendra.types.next_token


class ListDataSourceSyncJobsResponse(TypedDict):
    history: NotRequired[
        "aws_sdk_kendra.types.data_source_sync_job_history_list.DataSourceSyncJobHistoryList"
    ]
    """<p>A history of synchronization jobs for the data source connector.</p>"""
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Kendra returns this token that you can use in the subsequent request to retrieve the next set of jobs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataSourceSyncJobsResponse) -> dict:
    out: dict = {}
    if "history" in value:
        import aws_sdk_kendra.types.data_source_sync_job_history_list

        out["History"] = (
            aws_sdk_kendra.types.data_source_sync_job_history_list.serialize_aws_json_1_1(
                value["history"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataSourceSyncJobsResponse:
    out: ListDataSourceSyncJobsResponse = {}  # type: ignore[typeddict-item]
    if "History" in data:
        import aws_sdk_kendra.types.data_source_sync_job_history_list

        out["history"] = (
            aws_sdk_kendra.types.data_source_sync_job_history_list.deserialize_aws_json_1_1(
                data["History"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
