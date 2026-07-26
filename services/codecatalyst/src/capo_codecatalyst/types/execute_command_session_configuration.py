"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ExecuteCommandSessionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.execute_command_session_configuration_arguments


class ExecuteCommandSessionConfiguration(TypedDict, closed=True):
    command: "str"
    """<p>The command used at the beginning of the SSH session to a Dev Environment.</p>"""
    arguments: NotRequired[
        "capo_codecatalyst.types.execute_command_session_configuration_arguments.ExecuteCommandSessionConfigurationArguments"
    ]
    """<p>An array of arguments containing arguments and members.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteCommandSessionConfiguration) -> dict:
    out: dict = {}
    out["command"] = value["command"]
    if "arguments" in value:
        import capo_codecatalyst.types.execute_command_session_configuration_arguments

        out["arguments"] = (
            capo_codecatalyst.types.execute_command_session_configuration_arguments.serialize_json(
                value["arguments"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExecuteCommandSessionConfiguration:
    out: ExecuteCommandSessionConfiguration = {}  # type: ignore[typeddict-item]
    if "command" in data:
        out["command"] = data["command"]
    else:
        raise DeserializationError(
            "ExecuteCommandSessionConfiguration.command required"
        )
    if "arguments" in data:
        import capo_codecatalyst.types.execute_command_session_configuration_arguments

        out["arguments"] = (
            capo_codecatalyst.types.execute_command_session_configuration_arguments.deserialize_json(
                data["arguments"]
            )
        )
    return out
