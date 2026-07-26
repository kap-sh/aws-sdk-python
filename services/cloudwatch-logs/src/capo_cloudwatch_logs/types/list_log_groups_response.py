"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListLogGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_summaries
    import capo_cloudwatch_logs.types.next_token


class ListLogGroupsResponse(TypedDict, closed=True):
    log_groups: NotRequired[
        "capo_cloudwatch_logs.types.log_group_summaries.LogGroupSummaries"
    ]
    """<p>An array of structures, where each structure contains the information about one log group.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLogGroupsResponse) -> dict:
    out: dict = {}
    if "log_groups" in value:
        import capo_cloudwatch_logs.types.log_group_summaries

        out["logGroups"] = (
            capo_cloudwatch_logs.types.log_group_summaries.serialize_aws_json_1_1(
                value["log_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLogGroupsResponse:
    out: ListLogGroupsResponse = {}  # type: ignore[typeddict-item]
    if "logGroups" in data:
        import capo_cloudwatch_logs.types.log_group_summaries

        out["log_groups"] = (
            capo_cloudwatch_logs.types.log_group_summaries.deserialize_aws_json_1_1(
                data["logGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
