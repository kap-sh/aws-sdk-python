"""Generated from Smithy shape ``com.amazonaws.codecatalyst#StartDevEnvironmentSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.dev_environment_session_configuration
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.uuid


class StartDevEnvironmentSessionRequest(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "aws_sdk_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment.</p>"""
    session_configuration: "aws_sdk_codecatalyst.types.dev_environment_session_configuration.DevEnvironmentSessionConfiguration"


# --- restJson1 ser/de ---
def serialize_json(value: StartDevEnvironmentSessionRequest) -> dict:
    out: dict = {}
    import aws_sdk_codecatalyst.types.dev_environment_session_configuration

    out["sessionConfiguration"] = (
        aws_sdk_codecatalyst.types.dev_environment_session_configuration.serialize_json(
            value["session_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartDevEnvironmentSessionRequest:
    out: StartDevEnvironmentSessionRequest = {}  # type: ignore[typeddict-item]
    if "sessionConfiguration" in data:
        import aws_sdk_codecatalyst.types.dev_environment_session_configuration

        out["session_configuration"] = (
            aws_sdk_codecatalyst.types.dev_environment_session_configuration.deserialize_json(
                data["sessionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartDevEnvironmentSessionRequest.session_configuration required"
        )
    return out
