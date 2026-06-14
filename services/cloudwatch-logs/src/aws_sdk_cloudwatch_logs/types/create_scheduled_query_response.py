"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateScheduledQueryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.scheduled_query_state


class CreateScheduledQueryResponse(TypedDict):
    scheduled_query_arn: NotRequired["aws_sdk_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the created scheduled query.</p>"""
    state: NotRequired[
        "aws_sdk_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
    ]
    """<p>The current state of the scheduled query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateScheduledQueryResponse) -> dict:
    out: dict = {}
    if "scheduled_query_arn" in value:
        out["scheduledQueryArn"] = value["scheduled_query_arn"]
    if "state" in value:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateScheduledQueryResponse:
    out: CreateScheduledQueryResponse = {}  # type: ignore[typeddict-item]
    if "scheduledQueryArn" in data:
        out["scheduled_query_arn"] = data["scheduledQueryArn"]
    if "state" in data:
        import aws_sdk_cloudwatch_logs.types.scheduled_query_state

        out["state"] = (
            aws_sdk_cloudwatch_logs.types.scheduled_query_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    return out
