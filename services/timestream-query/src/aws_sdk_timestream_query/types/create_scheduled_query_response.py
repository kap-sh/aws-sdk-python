"""Generated from Smithy shape ``com.amazonaws.timestreamquery#CreateScheduledQueryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.amazon_resource_name


class CreateScheduledQueryResponse(TypedDict):
    arn: "aws_sdk_timestream_query.types.amazon_resource_name.AmazonResourceName"
    """<p>ARN for the created scheduled query.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateScheduledQueryResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateScheduledQueryResponse:
    out: CreateScheduledQueryResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CreateScheduledQueryResponse.arn required")
    return out
