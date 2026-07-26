"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetChannelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.channels_response


class GetChannelsResponse(TypedDict, closed=True):
    channels_response: NotRequired[
        "capo_pinpoint.types.channels_response.ChannelsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelsResponse) -> dict:
    out: dict = {}
    if "channels_response" in value:
        import capo_pinpoint.types.channels_response

        out["ChannelsResponse"] = capo_pinpoint.types.channels_response.serialize_json(
            value["channels_response"]
        )
    return out


def deserialize_json(data: dict) -> GetChannelsResponse:
    out: GetChannelsResponse = {}  # type: ignore[typeddict-item]
    if "ChannelsResponse" in data:
        import capo_pinpoint.types.channels_response

        out["channels_response"] = (
            capo_pinpoint.types.channels_response.deserialize_json(
                data["ChannelsResponse"]
            )
        )
    return out
