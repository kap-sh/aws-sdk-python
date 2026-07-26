"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetMessagingStreamingConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.streaming_configuration_list


class GetMessagingStreamingConfigurationsResponse(TypedDict, closed=True):
    streaming_configurations: NotRequired[
        "capo_chime_sdk_messaging.types.streaming_configuration_list.StreamingConfigurationList"
    ]
    """<p>The streaming settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMessagingStreamingConfigurationsResponse) -> dict:
    out: dict = {}
    if "streaming_configurations" in value:
        import capo_chime_sdk_messaging.types.streaming_configuration_list

        out["StreamingConfigurations"] = (
            capo_chime_sdk_messaging.types.streaming_configuration_list.serialize_json(
                value["streaming_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMessagingStreamingConfigurationsResponse:
    out: GetMessagingStreamingConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "StreamingConfigurations" in data:
        import capo_chime_sdk_messaging.types.streaming_configuration_list

        out["streaming_configurations"] = (
            capo_chime_sdk_messaging.types.streaming_configuration_list.deserialize_json(
                data["StreamingConfigurations"]
            )
        )
    return out
