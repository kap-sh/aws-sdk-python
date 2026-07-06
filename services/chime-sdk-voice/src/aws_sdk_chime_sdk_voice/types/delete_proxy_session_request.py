"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteProxySessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string128


class DeleteProxySessionRequest(TypedDict, closed=True):
    voice_connector_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""
    proxy_session_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The proxy session ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProxySessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProxySessionRequest:
    out: DeleteProxySessionRequest = {}  # type: ignore[typeddict-item]
    return out
