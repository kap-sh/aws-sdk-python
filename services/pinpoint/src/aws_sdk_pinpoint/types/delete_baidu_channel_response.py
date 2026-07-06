"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteBaiduChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.baidu_channel_response


class DeleteBaiduChannelResponse(TypedDict, closed=True):
    baidu_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.baidu_channel_response.BaiduChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBaiduChannelResponse) -> dict:
    out: dict = {}
    if "baidu_channel_response" in value:
        import aws_sdk_pinpoint.types.baidu_channel_response

        out["BaiduChannelResponse"] = (
            aws_sdk_pinpoint.types.baidu_channel_response.serialize_json(
                value["baidu_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteBaiduChannelResponse:
    out: DeleteBaiduChannelResponse = {}  # type: ignore[typeddict-item]
    if "BaiduChannelResponse" in data:
        import aws_sdk_pinpoint.types.baidu_channel_response

        out["baidu_channel_response"] = (
            aws_sdk_pinpoint.types.baidu_channel_response.deserialize_json(
                data["BaiduChannelResponse"]
            )
        )
    return out
