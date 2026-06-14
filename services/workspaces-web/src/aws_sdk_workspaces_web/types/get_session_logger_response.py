"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetSessionLoggerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.session_logger


class GetSessionLoggerResponse(TypedDict):
    session_logger: NotRequired[
        "aws_sdk_workspaces_web.types.session_logger.SessionLogger"
    ]
    """<p>The session logger details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionLoggerResponse) -> dict:
    out: dict = {}
    if "session_logger" in value:
        import aws_sdk_workspaces_web.types.session_logger

        out["sessionLogger"] = (
            aws_sdk_workspaces_web.types.session_logger.serialize_json(
                value["session_logger"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSessionLoggerResponse:
    out: GetSessionLoggerResponse = {}  # type: ignore[typeddict-item]
    if "sessionLogger" in data:
        import aws_sdk_workspaces_web.types.session_logger

        out["session_logger"] = (
            aws_sdk_workspaces_web.types.session_logger.deserialize_json(
                data["sessionLogger"]
            )
        )
    return out
