"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetBaiduChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.baidu_channel_response


class GetBaiduChannelResponse(TypedDict):
    baidu_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.baidu_channel_response.BaiduChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetBaiduChannelResponse) -> dict:
    out: dict = {}
    if "baidu_channel_response" in value:
        import aws_sdk_pinpoint.types.baidu_channel_response

        out["BaiduChannelResponse"] = (
            aws_sdk_pinpoint.types.baidu_channel_response.serialize_json(
                value["baidu_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBaiduChannelResponse:
    out: GetBaiduChannelResponse = {}  # type: ignore[typeddict-item]
    if "BaiduChannelResponse" in data:
        import aws_sdk_pinpoint.types.baidu_channel_response

        out["baidu_channel_response"] = (
            aws_sdk_pinpoint.types.baidu_channel_response.deserialize_json(
                data["BaiduChannelResponse"]
            )
        )
    return out
