"""Generated from Smithy shape ``com.amazonaws.directoryservice#SettingEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.setting_entry

SettingEntries: TypeAlias = list[
    "aws_sdk_directory_service.types.setting_entry.SettingEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SettingEntries) -> list:
    import aws_sdk_directory_service.types.setting_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_directory_service.types.setting_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SettingEntries:
    import aws_sdk_directory_service.types.setting_entry

    out: SettingEntries = []
    for item in data:
        out.append(
            aws_sdk_directory_service.types.setting_entry.deserialize_aws_json_1_1(item)
        )
    return out
