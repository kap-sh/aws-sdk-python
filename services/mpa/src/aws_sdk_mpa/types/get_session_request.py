"""Generated from Smithy shape ``com.amazonaws.mpa#GetSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mpa.types.session_arn


class GetSessionRequest(TypedDict, closed=True):
    session_arn: "aws_sdk_mpa.types.session_arn.SessionArn"
    """<p>Amazon Resource Name (ARN) for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionRequest:
    out: GetSessionRequest = {}  # type: ignore[typeddict-item]
    return out
