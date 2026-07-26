"""Generated from Smithy shape ``com.amazonaws.mpa#CancelSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.session_arn


class CancelSessionRequest(TypedDict, closed=True):
    session_arn: "capo_mpa.types.session_arn.SessionArn"
    """<p>Amazon Resource Name (ARN) for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelSessionRequest:
    out: CancelSessionRequest = {}  # type: ignore[typeddict-item]
    return out
