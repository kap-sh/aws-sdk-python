"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#DeleteMessagingStreamingConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn


class DeleteMessagingStreamingConfigurationsRequest(TypedDict, closed=True):
    app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the streaming configurations being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMessagingStreamingConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMessagingStreamingConfigurationsRequest:
    out: DeleteMessagingStreamingConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
