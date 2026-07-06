"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListProxySessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.next_token_string
    import aws_sdk_chime_sdk_voice.types.proxy_sessions


class ListProxySessionsResponse(TypedDict, closed=True):
    proxy_sessions: NotRequired[
        "aws_sdk_chime_sdk_voice.types.proxy_sessions.ProxySessions"
    ]
    """<p>The proxy sessions' details.</p>"""
    next_token: NotRequired[
        "aws_sdk_chime_sdk_voice.types.next_token_string.NextTokenString"
    ]
    """<p>The token used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProxySessionsResponse) -> dict:
    out: dict = {}
    if "proxy_sessions" in value:
        import aws_sdk_chime_sdk_voice.types.proxy_sessions

        out["ProxySessions"] = (
            aws_sdk_chime_sdk_voice.types.proxy_sessions.serialize_json(
                value["proxy_sessions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProxySessionsResponse:
    out: ListProxySessionsResponse = {}  # type: ignore[typeddict-item]
    if "ProxySessions" in data:
        import aws_sdk_chime_sdk_voice.types.proxy_sessions

        out["proxy_sessions"] = (
            aws_sdk_chime_sdk_voice.types.proxy_sessions.deserialize_json(
                data["ProxySessions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
