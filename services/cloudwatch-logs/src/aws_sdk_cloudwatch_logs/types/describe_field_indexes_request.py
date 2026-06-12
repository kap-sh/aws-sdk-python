"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeFieldIndexesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeFieldIndexesRequest(TypedDict):
    log_group_identifiers: "aws_sdk_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers.DescribeFieldIndexesLogGroupIdentifiers"
    """<p>An array containing the names or ARNs of the log groups that you want to retrieve field indexes for.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFieldIndexesRequest) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers

    out["logGroupIdentifiers"] = (
        aws_sdk_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers.serialize_aws_json_1_1(
            value["log_group_identifiers"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFieldIndexesRequest:
    out: DescribeFieldIndexesRequest = {}  # type: ignore[typeddict-item]
    if "logGroupIdentifiers" in data:
        import aws_sdk_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers

        out["log_group_identifiers"] = (
            aws_sdk_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers.deserialize_aws_json_1_1(
                data["logGroupIdentifiers"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeFieldIndexesRequest.log_group_identifiers required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
