"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.os_update_settings


class UpdateValue(TypedDict):
    os_update_settings: NotRequired[
        "aws_sdk_directory_service.types.os_update_settings.OSUpdateSettings"
    ]
    """<p> The OS update related settings. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateValue) -> dict:
    out: dict = {}
    if "os_update_settings" in value:
        import aws_sdk_directory_service.types.os_update_settings

        out["OSUpdateSettings"] = (
            aws_sdk_directory_service.types.os_update_settings.serialize_aws_json_1_1(
                value["os_update_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateValue:
    out: UpdateValue = {}  # type: ignore[typeddict-item]
    if "OSUpdateSettings" in data:
        import aws_sdk_directory_service.types.os_update_settings

        out["os_update_settings"] = (
            aws_sdk_directory_service.types.os_update_settings.deserialize_aws_json_1_1(
                data["OSUpdateSettings"]
            )
        )
    return out
