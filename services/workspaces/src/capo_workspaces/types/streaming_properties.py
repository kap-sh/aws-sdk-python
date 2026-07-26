"""Generated from Smithy shape ``com.amazonaws.workspaces#StreamingProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.global_accelerator_for_directory
    import capo_workspaces.types.storage_connectors
    import capo_workspaces.types.streaming_experience_preferred_protocol_enum
    import capo_workspaces.types.user_settings


class StreamingProperties(TypedDict, closed=True):
    streaming_experience_preferred_protocol: NotRequired[
        "capo_workspaces.types.streaming_experience_preferred_protocol_enum.StreamingExperiencePreferredProtocolEnum"
    ]
    """<p>Indicates the type of preferred protocol for the streaming experience.</p>"""
    user_settings: NotRequired["capo_workspaces.types.user_settings.UserSettings"]
    """<p>Indicates the permission settings asscoiated with the user.</p>"""
    storage_connectors: NotRequired[
        "capo_workspaces.types.storage_connectors.StorageConnectors"
    ]
    """<p>Indicates the storage connector used </p>"""
    global_accelerator: NotRequired[
        "capo_workspaces.types.global_accelerator_for_directory.GlobalAcceleratorForDirectory"
    ]
    """<p>Indicates the Global Accelerator properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamingProperties) -> dict:
    out: dict = {}
    if "streaming_experience_preferred_protocol" in value:
        import capo_workspaces.types.streaming_experience_preferred_protocol_enum

        out["StreamingExperiencePreferredProtocol"] = (
            capo_workspaces.types.streaming_experience_preferred_protocol_enum.serialize_aws_json_1_1(
                value["streaming_experience_preferred_protocol"]
            )
        )
    if "user_settings" in value:
        import capo_workspaces.types.user_settings

        out["UserSettings"] = (
            capo_workspaces.types.user_settings.serialize_aws_json_1_1(
                value["user_settings"]
            )
        )
    if "storage_connectors" in value:
        import capo_workspaces.types.storage_connectors

        out["StorageConnectors"] = (
            capo_workspaces.types.storage_connectors.serialize_aws_json_1_1(
                value["storage_connectors"]
            )
        )
    if "global_accelerator" in value:
        import capo_workspaces.types.global_accelerator_for_directory

        out["GlobalAccelerator"] = (
            capo_workspaces.types.global_accelerator_for_directory.serialize_aws_json_1_1(
                value["global_accelerator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamingProperties:
    out: StreamingProperties = {}  # type: ignore[typeddict-item]
    if "StreamingExperiencePreferredProtocol" in data:
        import capo_workspaces.types.streaming_experience_preferred_protocol_enum

        out["streaming_experience_preferred_protocol"] = (
            capo_workspaces.types.streaming_experience_preferred_protocol_enum.deserialize_aws_json_1_1(
                data["StreamingExperiencePreferredProtocol"]
            )
        )
    if "UserSettings" in data:
        import capo_workspaces.types.user_settings

        out["user_settings"] = (
            capo_workspaces.types.user_settings.deserialize_aws_json_1_1(
                data["UserSettings"]
            )
        )
    if "StorageConnectors" in data:
        import capo_workspaces.types.storage_connectors

        out["storage_connectors"] = (
            capo_workspaces.types.storage_connectors.deserialize_aws_json_1_1(
                data["StorageConnectors"]
            )
        )
    if "GlobalAccelerator" in data:
        import capo_workspaces.types.global_accelerator_for_directory

        out["global_accelerator"] = (
            capo_workspaces.types.global_accelerator_for_directory.deserialize_aws_json_1_1(
                data["GlobalAccelerator"]
            )
        )
    return out
