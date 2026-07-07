"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionLoggerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.display_name_safe
    import aws_sdk_workspaces_web.types.log_configuration
    import aws_sdk_workspaces_web.types.timestamp


class SessionLoggerSummary(TypedDict, closed=True):
    session_logger_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger resource.</p>"""
    log_configuration: NotRequired[
        "aws_sdk_workspaces_web.types.log_configuration.LogConfiguration"
    ]
    """<p>The configuration that specifies where the logs are fowarded.</p>"""
    display_name: NotRequired[
        "aws_sdk_workspaces_web.types.display_name_safe.DisplayNameSafe"
    ]
    """<p>The human-readable display name.</p>"""
    creation_date: NotRequired["aws_sdk_workspaces_web.types.timestamp.Timestamp"]
    """<p>The date the session logger resource was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionLoggerSummary) -> dict:
    out: dict = {}
    out["sessionLoggerArn"] = value["session_logger_arn"]
    if "log_configuration" in value:
        import aws_sdk_workspaces_web.types.log_configuration

        out["logConfiguration"] = (
            aws_sdk_workspaces_web.types.log_configuration.serialize_json(
                value["log_configuration"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "creation_date" in value:
        import aws_sdk_workspaces_web.types.timestamp

        out["creationDate"] = aws_sdk_workspaces_web.types.timestamp.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> SessionLoggerSummary:
    out: SessionLoggerSummary = {}  # type: ignore[typeddict-item]
    if "sessionLoggerArn" in data:
        out["session_logger_arn"] = data["sessionLoggerArn"]
    else:
        raise DeserializationError("SessionLoggerSummary.session_logger_arn required")
    if "logConfiguration" in data:
        import aws_sdk_workspaces_web.types.log_configuration

        out["log_configuration"] = (
            aws_sdk_workspaces_web.types.log_configuration.deserialize_json(
                data["logConfiguration"]
            )
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "creationDate" in data:
        import aws_sdk_workspaces_web.types.timestamp

        out["creation_date"] = aws_sdk_workspaces_web.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    return out
