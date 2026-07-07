"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateBaiduChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.baidu_channel_request


class UpdateBaiduChannelRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    baidu_channel_request: NotRequired[
        "aws_sdk_pinpoint.types.baidu_channel_request.BaiduChannelRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBaiduChannelRequest) -> dict:
    out: dict = {}
    if "baidu_channel_request" in value:
        import aws_sdk_pinpoint.types.baidu_channel_request

        out["BaiduChannelRequest"] = (
            aws_sdk_pinpoint.types.baidu_channel_request.serialize_json(
                value["baidu_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBaiduChannelRequest:
    out: UpdateBaiduChannelRequest = {}  # type: ignore[typeddict-item]
    if "BaiduChannelRequest" in data:
        import aws_sdk_pinpoint.types.baidu_channel_request

        out["baidu_channel_request"] = (
            aws_sdk_pinpoint.types.baidu_channel_request.deserialize_json(
                data["BaiduChannelRequest"]
            )
        )
    return out
