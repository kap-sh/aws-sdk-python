"""Generated from Smithy shape ``com.amazonaws.directoryservice#ClientAuthenticationSettingsInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.client_authentication_setting_info

ClientAuthenticationSettingsInfo: TypeAlias = list[
    "aws_sdk_directory_service.types.client_authentication_setting_info.ClientAuthenticationSettingInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientAuthenticationSettingsInfo) -> list:
    import aws_sdk_directory_service.types.client_authentication_setting_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_directory_service.types.client_authentication_setting_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClientAuthenticationSettingsInfo:
    import aws_sdk_directory_service.types.client_authentication_setting_info

    out: ClientAuthenticationSettingsInfo = []
    for item in data:
        out.append(
            aws_sdk_directory_service.types.client_authentication_setting_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
