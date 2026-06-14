"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InvocationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.arn


class InvocationConfiguration(TypedDict):
    topic_arn: "aws_sdk_bedrock_agentcore_control.types.arn.Arn"
    """<p>The ARN of the SNS topic for job notifications.</p>"""
    payload_delivery_bucket_name: "str"
    """<p>The S3 bucket name for event payload delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationConfiguration) -> dict:
    out: dict = {}
    out["topicArn"] = value["topic_arn"]
    out["payloadDeliveryBucketName"] = value["payload_delivery_bucket_name"]
    return out


def deserialize_json(data: dict) -> InvocationConfiguration:
    out: InvocationConfiguration = {}  # type: ignore[typeddict-item]
    if "topicArn" in data:
        out["topic_arn"] = data["topicArn"]
    else:
        raise DeserializationError("InvocationConfiguration.topic_arn required")
    if "payloadDeliveryBucketName" in data:
        out["payload_delivery_bucket_name"] = data["payloadDeliveryBucketName"]
    else:
        raise DeserializationError(
            "InvocationConfiguration.payload_delivery_bucket_name required"
        )
    return out
