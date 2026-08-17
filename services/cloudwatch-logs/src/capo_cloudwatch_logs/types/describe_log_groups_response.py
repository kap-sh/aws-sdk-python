"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeLogGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_groups
    import capo_cloudwatch_logs.types.next_token


class DescribeLogGroupsResponse(TypedDict, closed=True):
    log_groups: NotRequired["capo_cloudwatch_logs.types.log_groups.LogGroups"]
    """<p>An array of structures, where each structure contains the information about one log group.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLogGroupsResponse) -> dict:
    out: dict = {}
    if "log_groups" in value:
        import capo_cloudwatch_logs.types.log_groups

        out["logGroups"] = capo_cloudwatch_logs.types.log_groups.serialize_aws_json_1_1(
            value["log_groups"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLogGroupsResponse:
    out: DescribeLogGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("logGroups") is not None:
        import capo_cloudwatch_logs.types.log_groups

        out["log_groups"] = (
            capo_cloudwatch_logs.types.log_groups.deserialize_aws_json_1_1(
                data["logGroups"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
