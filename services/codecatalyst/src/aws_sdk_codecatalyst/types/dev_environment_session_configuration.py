"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentSessionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.dev_environment_session_type
    import aws_sdk_codecatalyst.types.execute_command_session_configuration


class DevEnvironmentSessionConfiguration(TypedDict, closed=True):
    session_type: "aws_sdk_codecatalyst.types.dev_environment_session_type.DevEnvironmentSessionType"
    """<p>The type of the session.</p>"""
    execute_command_session_configuration: NotRequired[
        "aws_sdk_codecatalyst.types.execute_command_session_configuration.ExecuteCommandSessionConfiguration"
    ]
    """<p>Information about optional commands that will be run on the Dev Environment when the SSH session begins.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentSessionConfiguration) -> dict:
    out: dict = {}
    out["sessionType"] = value["session_type"]
    if "execute_command_session_configuration" in value:
        import aws_sdk_codecatalyst.types.execute_command_session_configuration

        out["executeCommandSessionConfiguration"] = (
            aws_sdk_codecatalyst.types.execute_command_session_configuration.serialize_json(
                value["execute_command_session_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DevEnvironmentSessionConfiguration:
    out: DevEnvironmentSessionConfiguration = {}  # type: ignore[typeddict-item]
    if "sessionType" in data:
        out["session_type"] = data["sessionType"]
    else:
        raise DeserializationError(
            "DevEnvironmentSessionConfiguration.session_type required"
        )
    if "executeCommandSessionConfiguration" in data:
        import aws_sdk_codecatalyst.types.execute_command_session_configuration

        out["execute_command_session_configuration"] = (
            aws_sdk_codecatalyst.types.execute_command_session_configuration.deserialize_json(
                data["executeCommandSessionConfiguration"]
            )
        )
    return out
