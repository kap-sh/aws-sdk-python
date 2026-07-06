"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PutMessagingStreamingConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.streaming_configuration_list


class PutMessagingStreamingConfigurationsRequest(TypedDict, closed=True):
    app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the streaming configuration.</p>"""
    streaming_configurations: "aws_sdk_chime_sdk_messaging.types.streaming_configuration_list.StreamingConfigurationList"
    """<p>The streaming configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutMessagingStreamingConfigurationsRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_messaging.types.streaming_configuration_list

    out["StreamingConfigurations"] = (
        aws_sdk_chime_sdk_messaging.types.streaming_configuration_list.serialize_json(
            value["streaming_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutMessagingStreamingConfigurationsRequest:
    out: PutMessagingStreamingConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "StreamingConfigurations" in data:
        import aws_sdk_chime_sdk_messaging.types.streaming_configuration_list

        out["streaming_configurations"] = (
            aws_sdk_chime_sdk_messaging.types.streaming_configuration_list.deserialize_json(
                data["StreamingConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "PutMessagingStreamingConfigurationsRequest.streaming_configurations required"
        )
    return out
