"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DescribeScheduledQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.scheduled_query_description


class DescribeScheduledQueryResponse(TypedDict, closed=True):
    scheduled_query: "aws_sdk_timestream_query.types.scheduled_query_description.ScheduledQueryDescription"
    """<p>The scheduled query.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeScheduledQueryResponse) -> dict:
    out: dict = {}
    import aws_sdk_timestream_query.types.scheduled_query_description

    out["ScheduledQuery"] = (
        aws_sdk_timestream_query.types.scheduled_query_description.serialize_aws_json_1_0(
            value["scheduled_query"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeScheduledQueryResponse:
    out: DescribeScheduledQueryResponse = {}  # type: ignore[typeddict-item]
    if "ScheduledQuery" in data:
        import aws_sdk_timestream_query.types.scheduled_query_description

        out["scheduled_query"] = (
            aws_sdk_timestream_query.types.scheduled_query_description.deserialize_aws_json_1_0(
                data["ScheduledQuery"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeScheduledQueryResponse.scheduled_query required"
        )
    return out
