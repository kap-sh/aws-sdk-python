"""Generated from Smithy shape ``com.amazonaws.migrationhub#ListProgressUpdateStreamsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.progress_update_stream_summary_list
    import aws_sdk_migration_hub.types.token


class ListProgressUpdateStreamsResult(TypedDict, closed=True):
    progress_update_stream_summary_list: NotRequired[
        "aws_sdk_migration_hub.types.progress_update_stream_summary_list.ProgressUpdateStreamSummaryList"
    ]
    """<p>List of progress update streams up to the max number of results passed in the input.</p>"""
    next_token: NotRequired["aws_sdk_migration_hub.types.token.Token"]
    """<p>If there are more streams created than the max result, return the next token to be passed to the next call as a bookmark of where to start from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProgressUpdateStreamsResult) -> dict:
    out: dict = {}
    if "progress_update_stream_summary_list" in value:
        import aws_sdk_migration_hub.types.progress_update_stream_summary_list

        out["ProgressUpdateStreamSummaryList"] = (
            aws_sdk_migration_hub.types.progress_update_stream_summary_list.serialize_aws_json_1_1(
                value["progress_update_stream_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProgressUpdateStreamsResult:
    out: ListProgressUpdateStreamsResult = {}  # type: ignore[typeddict-item]
    if "ProgressUpdateStreamSummaryList" in data:
        import aws_sdk_migration_hub.types.progress_update_stream_summary_list

        out["progress_update_stream_summary_list"] = (
            aws_sdk_migration_hub.types.progress_update_stream_summary_list.deserialize_aws_json_1_1(
                data["ProgressUpdateStreamSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
