"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#LaunchOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.launch_command_list


class LaunchOverrides(TypedDict, closed=True):
    launch_commands: NotRequired[
        "aws_sdk_simspaceweaver.types.launch_command_list.LaunchCommandList"
    ]
    """<p>App launch commands and command line parameters that override the launch command configured in the simulation schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchOverrides) -> dict:
    out: dict = {}
    if "launch_commands" in value:
        import aws_sdk_simspaceweaver.types.launch_command_list

        out["LaunchCommands"] = (
            aws_sdk_simspaceweaver.types.launch_command_list.serialize_json(
                value["launch_commands"]
            )
        )
    return out


def deserialize_json(data: dict) -> LaunchOverrides:
    out: LaunchOverrides = {}  # type: ignore[typeddict-item]
    if "LaunchCommands" in data:
        import aws_sdk_simspaceweaver.types.launch_command_list

        out["launch_commands"] = (
            aws_sdk_simspaceweaver.types.launch_command_list.deserialize_json(
                data["LaunchCommands"]
            )
        )
    return out
