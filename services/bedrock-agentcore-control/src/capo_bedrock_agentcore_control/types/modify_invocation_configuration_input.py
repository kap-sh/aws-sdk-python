"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ModifyInvocationConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.arn


class ModifyInvocationConfigurationInput(TypedDict, closed=True):
    topic_arn: NotRequired["capo_bedrock_agentcore_control.types.arn.Arn"]
    """<p>The updated ARN of the SNS topic for job notifications.</p>"""
    payload_delivery_bucket_name: NotRequired["str"]
    """<p>The updated S3 bucket name for event payload delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModifyInvocationConfigurationInput) -> dict:
    out: dict = {}
    if "topic_arn" in value:
        out["topicArn"] = value["topic_arn"]
    if "payload_delivery_bucket_name" in value:
        out["payloadDeliveryBucketName"] = value["payload_delivery_bucket_name"]
    return out


def deserialize_json(data: dict) -> ModifyInvocationConfigurationInput:
    out: ModifyInvocationConfigurationInput = {}  # type: ignore[typeddict-item]
    if "topicArn" in data:
        out["topic_arn"] = data["topicArn"]
    if "payloadDeliveryBucketName" in data:
        out["payload_delivery_bucket_name"] = data["payloadDeliveryBucketName"]
    return out
