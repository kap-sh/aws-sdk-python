"""Generated from Smithy shape ``com.amazonaws.mpa#CancelSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mpa.types.session_arn


class CancelSessionRequest(TypedDict):
    session_arn: "aws_sdk_mpa.types.session_arn.SessionArn"
    """<p>Amazon Resource Name (ARN) for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelSessionRequest:
    out: CancelSessionRequest = {}  # type: ignore[typeddict-item]
    return out
