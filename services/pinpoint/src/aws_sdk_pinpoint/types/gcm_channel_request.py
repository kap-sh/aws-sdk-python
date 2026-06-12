"""Generated from Smithy shape ``com.amazonaws.pinpoint#GCMChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__boolean
    import aws_sdk_pinpoint.types.__string


class GCMChannelRequest(TypedDict):
    api_key: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The Web API Key, also referred to as an <i>API_KEY</i> or <i>server key</i>, that you received from Google to communicate with Google services.</p>"""
    default_authentication_method: NotRequired[
        "aws_sdk_pinpoint.types.__string.__string"
    ]
    """<p>The default authentication method used for GCM. Values are either \"TOKEN\" or \"KEY\". Defaults to \"KEY\".</p>"""
    enabled: NotRequired["aws_sdk_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to enable the GCM channel for the application.</p>"""
    service_json: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The contents of the JSON file provided by Google during registration in order to generate an access token for authentication. For more information see <a href=\"https://firebase.google.com/docs/cloud-messaging/migrate-v1\">Migrate from legacy FCM APIs to HTTP v1</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GCMChannelRequest) -> dict:
    out: dict = {}
    if "api_key" in value:
        out["ApiKey"] = value["api_key"]
    if "default_authentication_method" in value:
        out["DefaultAuthenticationMethod"] = value["default_authentication_method"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "service_json" in value:
        out["ServiceJson"] = value["service_json"]
    return out


def deserialize_json(data: dict) -> GCMChannelRequest:
    out: GCMChannelRequest = {}  # type: ignore[typeddict-item]
    if "ApiKey" in data:
        out["api_key"] = data["ApiKey"]
    if "DefaultAuthenticationMethod" in data:
        out["default_authentication_method"] = data["DefaultAuthenticationMethod"]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "ServiceJson" in data:
        out["service_json"] = data["ServiceJson"]
    return out
