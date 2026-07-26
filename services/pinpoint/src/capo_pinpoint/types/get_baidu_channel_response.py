"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetBaiduChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.baidu_channel_response


class GetBaiduChannelResponse(TypedDict, closed=True):
    baidu_channel_response: NotRequired[
        "capo_pinpoint.types.baidu_channel_response.BaiduChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetBaiduChannelResponse) -> dict:
    out: dict = {}
    if "baidu_channel_response" in value:
        import capo_pinpoint.types.baidu_channel_response

        out["BaiduChannelResponse"] = (
            capo_pinpoint.types.baidu_channel_response.serialize_json(
                value["baidu_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBaiduChannelResponse:
    out: GetBaiduChannelResponse = {}  # type: ignore[typeddict-item]
    if "BaiduChannelResponse" in data:
        import capo_pinpoint.types.baidu_channel_response

        out["baidu_channel_response"] = (
            capo_pinpoint.types.baidu_channel_response.deserialize_json(
                data["BaiduChannelResponse"]
            )
        )
    return out
