"""Generated from Smithy shape ``com.amazonaws.workspaces#StreamingProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.global_accelerator_for_directory
    import aws_sdk_workspaces.types.storage_connectors
    import aws_sdk_workspaces.types.streaming_experience_preferred_protocol_enum
    import aws_sdk_workspaces.types.user_settings


class StreamingProperties(TypedDict):
    streaming_experience_preferred_protocol: NotRequired[
        "aws_sdk_workspaces.types.streaming_experience_preferred_protocol_enum.StreamingExperiencePreferredProtocolEnum"
    ]
    """<p>Indicates the type of preferred protocol for the streaming experience.</p>"""
    user_settings: NotRequired["aws_sdk_workspaces.types.user_settings.UserSettings"]
    """<p>Indicates the permission settings asscoiated with the user.</p>"""
    storage_connectors: NotRequired[
        "aws_sdk_workspaces.types.storage_connectors.StorageConnectors"
    ]
    """<p>Indicates the storage connector used </p>"""
    global_accelerator: NotRequired[
        "aws_sdk_workspaces.types.global_accelerator_for_directory.GlobalAcceleratorForDirectory"
    ]
    """<p>Indicates the Global Accelerator properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamingProperties) -> dict:
    out: dict = {}
    if "streaming_experience_preferred_protocol" in value:
        import aws_sdk_workspaces.types.streaming_experience_preferred_protocol_enum

        out["StreamingExperiencePreferredProtocol"] = (
            aws_sdk_workspaces.types.streaming_experience_preferred_protocol_enum.serialize_aws_json_1_1(
                value["streaming_experience_preferred_protocol"]
            )
        )
    if "user_settings" in value:
        import aws_sdk_workspaces.types.user_settings

        out["UserSettings"] = (
            aws_sdk_workspaces.types.user_settings.serialize_aws_json_1_1(
                value["user_settings"]
            )
        )
    if "storage_connectors" in value:
        import aws_sdk_workspaces.types.storage_connectors

        out["StorageConnectors"] = (
            aws_sdk_workspaces.types.storage_connectors.serialize_aws_json_1_1(
                value["storage_connectors"]
            )
        )
    if "global_accelerator" in value:
        import aws_sdk_workspaces.types.global_accelerator_for_directory

        out["GlobalAccelerator"] = (
            aws_sdk_workspaces.types.global_accelerator_for_directory.serialize_aws_json_1_1(
                value["global_accelerator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamingProperties:
    out: StreamingProperties = {}  # type: ignore[typeddict-item]
    if "StreamingExperiencePreferredProtocol" in data:
        import aws_sdk_workspaces.types.streaming_experience_preferred_protocol_enum

        out["streaming_experience_preferred_protocol"] = (
            aws_sdk_workspaces.types.streaming_experience_preferred_protocol_enum.deserialize_aws_json_1_1(
                data["StreamingExperiencePreferredProtocol"]
            )
        )
    if "UserSettings" in data:
        import aws_sdk_workspaces.types.user_settings

        out["user_settings"] = (
            aws_sdk_workspaces.types.user_settings.deserialize_aws_json_1_1(
                data["UserSettings"]
            )
        )
    if "StorageConnectors" in data:
        import aws_sdk_workspaces.types.storage_connectors

        out["storage_connectors"] = (
            aws_sdk_workspaces.types.storage_connectors.deserialize_aws_json_1_1(
                data["StorageConnectors"]
            )
        )
    if "GlobalAccelerator" in data:
        import aws_sdk_workspaces.types.global_accelerator_for_directory

        out["global_accelerator"] = (
            aws_sdk_workspaces.types.global_accelerator_for_directory.deserialize_aws_json_1_1(
                data["GlobalAccelerator"]
            )
        )
    return out
