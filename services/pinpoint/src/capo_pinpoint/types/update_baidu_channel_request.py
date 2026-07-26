"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateBaiduChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.baidu_channel_request


class UpdateBaiduChannelRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    baidu_channel_request: NotRequired[
        "capo_pinpoint.types.baidu_channel_request.BaiduChannelRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBaiduChannelRequest) -> dict:
    out: dict = {}
    if "baidu_channel_request" in value:
        import capo_pinpoint.types.baidu_channel_request

        out["BaiduChannelRequest"] = (
            capo_pinpoint.types.baidu_channel_request.serialize_json(
                value["baidu_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBaiduChannelRequest:
    out: UpdateBaiduChannelRequest = {}  # type: ignore[typeddict-item]
    if "BaiduChannelRequest" in data:
        import capo_pinpoint.types.baidu_channel_request

        out["baidu_channel_request"] = (
            capo_pinpoint.types.baidu_channel_request.deserialize_json(
                data["BaiduChannelRequest"]
            )
        )
    return out
