"""Generated from Smithy shape ``com.amazonaws.workspaces#GlobalAcceleratorForDirectory``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.aga_mode_for_directory_enum
    import aws_sdk_workspaces.types.aga_preferred_protocol_for_directory


class GlobalAcceleratorForDirectory(TypedDict):
    mode: "aws_sdk_workspaces.types.aga_mode_for_directory_enum.AGAModeForDirectoryEnum"
    """<p>Indicates if Global Accelerator for directory is enabled or disabled.</p>"""
    preferred_protocol: NotRequired[
        "aws_sdk_workspaces.types.aga_preferred_protocol_for_directory.AGAPreferredProtocolForDirectory"
    ]
    """<p>Indicates the preferred protocol for Global Accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlobalAcceleratorForDirectory) -> dict:
    out: dict = {}
    import aws_sdk_workspaces.types.aga_mode_for_directory_enum

    out["Mode"] = (
        aws_sdk_workspaces.types.aga_mode_for_directory_enum.serialize_aws_json_1_1(
            value["mode"]
        )
    )
    if "preferred_protocol" in value:
        import aws_sdk_workspaces.types.aga_preferred_protocol_for_directory

        out["PreferredProtocol"] = (
            aws_sdk_workspaces.types.aga_preferred_protocol_for_directory.serialize_aws_json_1_1(
                value["preferred_protocol"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GlobalAcceleratorForDirectory:
    out: GlobalAcceleratorForDirectory = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import aws_sdk_workspaces.types.aga_mode_for_directory_enum

        out["mode"] = (
            aws_sdk_workspaces.types.aga_mode_for_directory_enum.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    else:
        raise DeserializationError("GlobalAcceleratorForDirectory.mode required")
    if "PreferredProtocol" in data:
        import aws_sdk_workspaces.types.aga_preferred_protocol_for_directory

        out["preferred_protocol"] = (
            aws_sdk_workspaces.types.aga_preferred_protocol_for_directory.deserialize_aws_json_1_1(
                data["PreferredProtocol"]
            )
        )
    return out
