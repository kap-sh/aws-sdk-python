"""Generated from Smithy shape ``com.amazonaws.timestreamquery#UpdateScheduledQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.amazon_resource_name
    import aws_sdk_timestream_query.types.scheduled_query_state


class UpdateScheduledQueryRequest(TypedDict, closed=True):
    scheduled_query_arn: (
        "aws_sdk_timestream_query.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>ARN of the scheuled query.</p>"""
    state: "aws_sdk_timestream_query.types.scheduled_query_state.ScheduledQueryState"
    """<p>State of the scheduled query. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateScheduledQueryRequest) -> dict:
    out: dict = {}
    out["ScheduledQueryArn"] = value["scheduled_query_arn"]
    import aws_sdk_timestream_query.types.scheduled_query_state

    out["State"] = (
        aws_sdk_timestream_query.types.scheduled_query_state.serialize_aws_json_1_0(
            value["state"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateScheduledQueryRequest:
    out: UpdateScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if "ScheduledQueryArn" in data:
        out["scheduled_query_arn"] = data["ScheduledQueryArn"]
    else:
        raise DeserializationError(
            "UpdateScheduledQueryRequest.scheduled_query_arn required"
        )
    if "State" in data:
        import aws_sdk_timestream_query.types.scheduled_query_state

        out["state"] = (
            aws_sdk_timestream_query.types.scheduled_query_state.deserialize_aws_json_1_0(
                data["State"]
            )
        )
    else:
        raise DeserializationError("UpdateScheduledQueryRequest.state required")
    return out
