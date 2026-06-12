"""Generated from Smithy shape ``com.amazonaws.iot#GetTopicRuleDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn


class GetTopicRuleDestinationRequest(TypedDict):
    arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the topic rule destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTopicRuleDestinationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTopicRuleDestinationRequest:
    out: GetTopicRuleDestinationRequest = {}  # type: ignore[typeddict-item]
    return out
