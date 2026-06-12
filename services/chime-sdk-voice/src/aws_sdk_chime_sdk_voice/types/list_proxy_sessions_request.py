"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListProxySessionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.next_token_string
    import aws_sdk_chime_sdk_voice.types.non_empty_string128
    import aws_sdk_chime_sdk_voice.types.proxy_session_status
    import aws_sdk_chime_sdk_voice.types.result_max


class ListProxySessionsRequest(TypedDict):
    voice_connector_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""
    status: NotRequired[
        "aws_sdk_chime_sdk_voice.types.proxy_session_status.ProxySessionStatus"
    ]
    """<p>The proxy session status.</p>"""
    next_token: NotRequired[
        "aws_sdk_chime_sdk_voice.types.next_token_string.NextTokenString"
    ]
    """<p>The token used to retrieve the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_chime_sdk_voice.types.result_max.ResultMax"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProxySessionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProxySessionsRequest:
    out: ListProxySessionsRequest = {}  # type: ignore[typeddict-item]
    return out
