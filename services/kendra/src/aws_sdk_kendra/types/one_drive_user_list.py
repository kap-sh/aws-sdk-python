"""Generated from Smithy shape ``com.amazonaws.kendra#OneDriveUserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.one_drive_user

OneDriveUserList: TypeAlias = list["aws_sdk_kendra.types.one_drive_user.OneDriveUser"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OneDriveUserList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OneDriveUserList:
    return list(data)
