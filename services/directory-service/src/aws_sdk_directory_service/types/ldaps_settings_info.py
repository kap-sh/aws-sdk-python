"""Generated from Smithy shape ``com.amazonaws.directoryservice#LDAPSSettingsInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.ldaps_setting_info

LDAPSSettingsInfo: TypeAlias = list[
    "aws_sdk_directory_service.types.ldaps_setting_info.LDAPSSettingInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LDAPSSettingsInfo) -> list:
    import aws_sdk_directory_service.types.ldaps_setting_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_directory_service.types.ldaps_setting_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LDAPSSettingsInfo:
    import aws_sdk_directory_service.types.ldaps_setting_info

    out: LDAPSSettingsInfo = []
    for item in data:
        out.append(
            aws_sdk_directory_service.types.ldaps_setting_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
