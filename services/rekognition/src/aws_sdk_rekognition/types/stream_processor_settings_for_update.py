"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorSettingsForUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.connected_home_settings_for_update


class StreamProcessorSettingsForUpdate(TypedDict):
    connected_home_for_update: NotRequired[
        "aws_sdk_rekognition.types.connected_home_settings_for_update.ConnectedHomeSettingsForUpdate"
    ]
    """<p> The label detection settings you want to use for your stream processor. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessorSettingsForUpdate) -> dict:
    out: dict = {}
    if "connected_home_for_update" in value:
        import aws_sdk_rekognition.types.connected_home_settings_for_update

        out["ConnectedHomeForUpdate"] = (
            aws_sdk_rekognition.types.connected_home_settings_for_update.serialize_aws_json_1_1(
                value["connected_home_for_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamProcessorSettingsForUpdate:
    out: StreamProcessorSettingsForUpdate = {}  # type: ignore[typeddict-item]
    if "ConnectedHomeForUpdate" in data:
        import aws_sdk_rekognition.types.connected_home_settings_for_update

        out["connected_home_for_update"] = (
            aws_sdk_rekognition.types.connected_home_settings_for_update.deserialize_aws_json_1_1(
                data["ConnectedHomeForUpdate"]
            )
        )
    return out
