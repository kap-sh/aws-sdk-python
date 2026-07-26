"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateProxySessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.proxy_session


class UpdateProxySessionResponse(TypedDict, closed=True):
    proxy_session: NotRequired["capo_chime_sdk_voice.types.proxy_session.ProxySession"]
    """<p>The updated proxy session details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProxySessionResponse) -> dict:
    out: dict = {}
    if "proxy_session" in value:
        import capo_chime_sdk_voice.types.proxy_session

        out["ProxySession"] = capo_chime_sdk_voice.types.proxy_session.serialize_json(
            value["proxy_session"]
        )
    return out


def deserialize_json(data: dict) -> UpdateProxySessionResponse:
    out: UpdateProxySessionResponse = {}  # type: ignore[typeddict-item]
    if "ProxySession" in data:
        import capo_chime_sdk_voice.types.proxy_session

        out["proxy_session"] = (
            capo_chime_sdk_voice.types.proxy_session.deserialize_json(
                data["ProxySession"]
            )
        )
    return out
