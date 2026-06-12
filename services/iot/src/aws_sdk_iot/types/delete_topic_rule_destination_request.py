"""Generated from Smithy shape ``com.amazonaws.iot#DeleteTopicRuleDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn


class DeleteTopicRuleDestinationRequest(TypedDict):
    arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the topic rule destination to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTopicRuleDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTopicRuleDestinationRequest:
    out: DeleteTopicRuleDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
