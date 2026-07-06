"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantIntegrationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.generic_arn


class AssistantIntegrationConfiguration(TypedDict, closed=True):
    topic_integration_arn: NotRequired["aws_sdk_qconnect.types.generic_arn.GenericArn"]
    """<p>The Amazon Resource Name (ARN) of the integrated Amazon SNS topic used for streaming chat messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssistantIntegrationConfiguration) -> dict:
    out: dict = {}
    if "topic_integration_arn" in value:
        out["topicIntegrationArn"] = value["topic_integration_arn"]
    return out


def deserialize_json(data: dict) -> AssistantIntegrationConfiguration:
    out: AssistantIntegrationConfiguration = {}  # type: ignore[typeddict-item]
    if "topicIntegrationArn" in data:
        out["topic_integration_arn"] = data["topicIntegrationArn"]
    return out
