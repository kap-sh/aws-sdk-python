"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateSessionLoggerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.session_logger


class UpdateSessionLoggerResponse(TypedDict, closed=True):
    session_logger: "aws_sdk_workspaces_web.types.session_logger.SessionLogger"
    """<p>The updated details of the session logger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionLoggerResponse) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_web.types.session_logger

    out["sessionLogger"] = aws_sdk_workspaces_web.types.session_logger.serialize_json(
        value["session_logger"]
    )
    return out


def deserialize_json(data: dict) -> UpdateSessionLoggerResponse:
    out: UpdateSessionLoggerResponse = {}  # type: ignore[typeddict-item]
    if "sessionLogger" in data:
        import aws_sdk_workspaces_web.types.session_logger

        out["session_logger"] = (
            aws_sdk_workspaces_web.types.session_logger.deserialize_json(
                data["sessionLogger"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSessionLoggerResponse.session_logger required"
        )
    return out
