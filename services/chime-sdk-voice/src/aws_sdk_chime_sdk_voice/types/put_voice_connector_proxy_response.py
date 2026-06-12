"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorProxyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.proxy


class PutVoiceConnectorProxyResponse(TypedDict):
    proxy: NotRequired["aws_sdk_chime_sdk_voice.types.proxy.Proxy"]
    """<p>The proxy configuration details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorProxyResponse) -> dict:
    out: dict = {}
    if "proxy" in value:
        import aws_sdk_chime_sdk_voice.types.proxy

        out["Proxy"] = aws_sdk_chime_sdk_voice.types.proxy.serialize_json(
            value["proxy"]
        )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorProxyResponse:
    out: PutVoiceConnectorProxyResponse = {}  # type: ignore[typeddict-item]
    if "Proxy" in data:
        import aws_sdk_chime_sdk_voice.types.proxy

        out["proxy"] = aws_sdk_chime_sdk_voice.types.proxy.deserialize_json(
            data["Proxy"]
        )
    return out
