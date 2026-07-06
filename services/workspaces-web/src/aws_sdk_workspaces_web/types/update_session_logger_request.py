"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateSessionLoggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.display_name_safe
    import aws_sdk_workspaces_web.types.event_filter
    import aws_sdk_workspaces_web.types.log_configuration


class UpdateSessionLoggerRequest(TypedDict, closed=True):
    session_logger_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger to update.</p>"""
    event_filter: NotRequired["aws_sdk_workspaces_web.types.event_filter.EventFilter"]
    """<p>The updated eventFilter.</p>"""
    log_configuration: NotRequired[
        "aws_sdk_workspaces_web.types.log_configuration.LogConfiguration"
    ]
    """<p>The updated logConfiguration.</p>"""
    display_name: NotRequired[
        "aws_sdk_workspaces_web.types.display_name_safe.DisplayNameSafe"
    ]
    """<p>The updated display name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionLoggerRequest) -> dict:
    out: dict = {}
    if "event_filter" in value:
        import aws_sdk_workspaces_web.types.event_filter

        out["eventFilter"] = aws_sdk_workspaces_web.types.event_filter.serialize_json(
            value["event_filter"]
        )
    if "log_configuration" in value:
        import aws_sdk_workspaces_web.types.log_configuration

        out["logConfiguration"] = (
            aws_sdk_workspaces_web.types.log_configuration.serialize_json(
                value["log_configuration"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> UpdateSessionLoggerRequest:
    out: UpdateSessionLoggerRequest = {}  # type: ignore[typeddict-item]
    if "eventFilter" in data:
        import aws_sdk_workspaces_web.types.event_filter

        out["event_filter"] = (
            aws_sdk_workspaces_web.types.event_filter.deserialize_json(
                data["eventFilter"]
            )
        )
    if "logConfiguration" in data:
        import aws_sdk_workspaces_web.types.log_configuration

        out["log_configuration"] = (
            aws_sdk_workspaces_web.types.log_configuration.deserialize_json(
                data["logConfiguration"]
            )
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    return out
