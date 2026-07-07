"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListLogGroupsForQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_identifiers
    import aws_sdk_cloudwatch_logs.types.next_token


class ListLogGroupsForQueryResponse(TypedDict, closed=True):
    log_group_identifiers: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_identifiers.LogGroupIdentifiers"
    ]
    """<p>An array of the names and ARNs of the log groups that were processed in the query.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLogGroupsForQueryResponse) -> dict:
    out: dict = {}
    if "log_group_identifiers" in value:
        import aws_sdk_cloudwatch_logs.types.log_group_identifiers

        out["logGroupIdentifiers"] = (
            aws_sdk_cloudwatch_logs.types.log_group_identifiers.serialize_aws_json_1_1(
                value["log_group_identifiers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLogGroupsForQueryResponse:
    out: ListLogGroupsForQueryResponse = {}  # type: ignore[typeddict-item]
    if "logGroupIdentifiers" in data:
        import aws_sdk_cloudwatch_logs.types.log_group_identifiers

        out["log_group_identifiers"] = (
            aws_sdk_cloudwatch_logs.types.log_group_identifiers.deserialize_aws_json_1_1(
                data["logGroupIdentifiers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
