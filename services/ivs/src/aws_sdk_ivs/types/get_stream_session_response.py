"""Generated from Smithy shape ``com.amazonaws.ivs#GetStreamSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.stream_session


class GetStreamSessionResponse(TypedDict, closed=True):
    stream_session: NotRequired["aws_sdk_ivs.types.stream_session.StreamSession"]
    """<p>List of stream details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamSessionResponse) -> dict:
    out: dict = {}
    if "stream_session" in value:
        import aws_sdk_ivs.types.stream_session

        out["streamSession"] = aws_sdk_ivs.types.stream_session.serialize_json(
            value["stream_session"]
        )
    return out


def deserialize_json(data: dict) -> GetStreamSessionResponse:
    out: GetStreamSessionResponse = {}  # type: ignore[typeddict-item]
    if "streamSession" in data:
        import aws_sdk_ivs.types.stream_session

        out["stream_session"] = aws_sdk_ivs.types.stream_session.deserialize_json(
            data["streamSession"]
        )
    return out
