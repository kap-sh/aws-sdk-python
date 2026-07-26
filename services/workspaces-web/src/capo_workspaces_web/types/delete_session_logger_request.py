"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DeleteSessionLoggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class DeleteSessionLoggerRequest(TypedDict, closed=True):
    session_logger_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSessionLoggerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSessionLoggerRequest:
    out: DeleteSessionLoggerRequest = {}  # type: ignore[typeddict-item]
    return out
