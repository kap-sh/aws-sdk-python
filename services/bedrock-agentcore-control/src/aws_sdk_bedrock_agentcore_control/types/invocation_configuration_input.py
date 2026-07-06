"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InvocationConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.arn


class InvocationConfigurationInput(TypedDict, closed=True):
    topic_arn: "aws_sdk_bedrock_agentcore_control.types.arn.Arn"
    """<p>The ARN of the SNS topic for job notifications.</p>"""
    payload_delivery_bucket_name: "str"
    """<p>The S3 bucket name for event payload delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationConfigurationInput) -> dict:
    out: dict = {}
    out["topicArn"] = value["topic_arn"]
    out["payloadDeliveryBucketName"] = value["payload_delivery_bucket_name"]
    return out


def deserialize_json(data: dict) -> InvocationConfigurationInput:
    out: InvocationConfigurationInput = {}  # type: ignore[typeddict-item]
    if "topicArn" in data:
        out["topic_arn"] = data["topicArn"]
    else:
        raise DeserializationError("InvocationConfigurationInput.topic_arn required")
    if "payloadDeliveryBucketName" in data:
        out["payload_delivery_bucket_name"] = data["payloadDeliveryBucketName"]
    else:
        raise DeserializationError(
            "InvocationConfigurationInput.payload_delivery_bucket_name required"
        )
    return out
