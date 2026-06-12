"""Generated from Smithy shape ``com.amazonaws.kinesis#PutResourcePolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.policy
    import aws_sdk_kinesis.types.resource_arn
    import aws_sdk_kinesis.types.stream_id


class PutResourcePolicyInput(TypedDict):
    resource_arn: "aws_sdk_kinesis.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the data stream or consumer.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    policy: "aws_sdk_kinesis.types.policy.Policy"
    """<p>Details of the resource policy. It must include the identity of the principal and the actions allowed on this resource. This is formatted as a JSON string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyInput:
    out: PutResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("PutResourcePolicyInput.resource_arn required")
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutResourcePolicyInput.policy required")
    return out
