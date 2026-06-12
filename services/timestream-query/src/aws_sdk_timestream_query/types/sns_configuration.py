"""Generated from Smithy shape ``com.amazonaws.timestreamquery#SnsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.amazon_resource_name


class SnsConfiguration(TypedDict):
    topic_arn: "aws_sdk_timestream_query.types.amazon_resource_name.AmazonResourceName"
    """<p>SNS topic ARN that the scheduled query status notifications will be sent to.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SnsConfiguration) -> dict:
    out: dict = {}
    out["TopicArn"] = value["topic_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SnsConfiguration:
    out: SnsConfiguration = {}  # type: ignore[typeddict-item]
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    else:
        raise DeserializationError("SnsConfiguration.topic_arn required")
    return out
