"""Generated from Smithy shape ``com.amazonaws.iot#PublishFindingToSnsParams``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.sns_topic_arn


class PublishFindingToSnsParams(TypedDict, closed=True):
    topic_arn: "aws_sdk_iot.types.sns_topic_arn.SnsTopicArn"
    """<p>The ARN of the topic to which you want to publish the findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishFindingToSnsParams) -> dict:
    out: dict = {}
    out["topicArn"] = value["topic_arn"]
    return out


def deserialize_json(data: dict) -> PublishFindingToSnsParams:
    out: PublishFindingToSnsParams = {}  # type: ignore[typeddict-item]
    if "topicArn" in data:
        out["topic_arn"] = data["topicArn"]
    else:
        raise DeserializationError("PublishFindingToSnsParams.topic_arn required")
    return out
