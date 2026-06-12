"""Generated from Smithy shape ``com.amazonaws.pinpoint#BaiduChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean
    import aws_sdk_pinpoint.types.__string


class BaiduChannelRequest(TypedDict):
    api_key: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The API key that you received from the Baidu Cloud Push service to communicate with the service.</p>"""
    enabled: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to enable the Baidu channel for the application.</p>"""
    secret_key: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The secret key that you received from the Baidu Cloud Push service to communicate with the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BaiduChannelRequest) -> dict:
    out: dict = {}
    if "api_key" in value:
        out["ApiKey"] = value["api_key"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "secret_key" in value:
        out["SecretKey"] = value["secret_key"]
    return out


def deserialize_json(data: dict) -> BaiduChannelRequest:
    out: BaiduChannelRequest = {}  # type: ignore[typeddict-item]
    if "ApiKey" in data:
        out["api_key"] = data["ApiKey"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "SecretKey" in data:
        out["secret_key"] = data["SecretKey"]
    return out
