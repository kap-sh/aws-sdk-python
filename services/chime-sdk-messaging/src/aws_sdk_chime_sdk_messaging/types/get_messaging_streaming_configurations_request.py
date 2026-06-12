"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetMessagingStreamingConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class GetMessagingStreamingConfigurationsRequest(TypedDict):
    app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the streaming configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMessagingStreamingConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMessagingStreamingConfigurationsRequest:
    out: GetMessagingStreamingConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
