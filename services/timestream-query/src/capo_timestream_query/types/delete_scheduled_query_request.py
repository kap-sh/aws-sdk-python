"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DeleteScheduledQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name


class DeleteScheduledQueryRequest(TypedDict, closed=True):
    scheduled_query_arn: (
        "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN of the scheduled query. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteScheduledQueryRequest) -> dict:
    out: dict = {}
    out["ScheduledQueryArn"] = value["scheduled_query_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteScheduledQueryRequest:
    out: DeleteScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if "ScheduledQueryArn" in data:
        out["scheduled_query_arn"] = data["ScheduledQueryArn"]
    else:
        raise DeserializationError(
            "DeleteScheduledQueryRequest.scheduled_query_arn required"
        )
    return out
