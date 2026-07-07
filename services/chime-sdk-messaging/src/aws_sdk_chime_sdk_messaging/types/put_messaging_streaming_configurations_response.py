"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PutMessagingStreamingConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.streaming_configuration_list


class PutMessagingStreamingConfigurationsResponse(TypedDict, closed=True):
    streaming_configurations: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.streaming_configuration_list.StreamingConfigurationList"
    ]
    """<p>The requested streaming configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutMessagingStreamingConfigurationsResponse) -> dict:
    out: dict = {}
    if "streaming_configurations" in value:
        import aws_sdk_chime_sdk_messaging.types.streaming_configuration_list

        out["StreamingConfigurations"] = (
            aws_sdk_chime_sdk_messaging.types.streaming_configuration_list.serialize_json(
                value["streaming_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutMessagingStreamingConfigurationsResponse:
    out: PutMessagingStreamingConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "StreamingConfigurations" in data:
        import aws_sdk_chime_sdk_messaging.types.streaming_configuration_list

        out["streaming_configurations"] = (
            aws_sdk_chime_sdk_messaging.types.streaming_configuration_list.deserialize_json(
                data["StreamingConfigurations"]
            )
        )
    return out
