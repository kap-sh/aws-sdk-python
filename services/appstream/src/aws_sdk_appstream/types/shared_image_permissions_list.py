"""Generated from Smithy shape ``com.amazonaws.appstream#SharedImagePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.shared_image_permissions

SharedImagePermissionsList: TypeAlias = list[
    "aws_sdk_appstream.types.shared_image_permissions.SharedImagePermissions"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharedImagePermissionsList) -> list:
    import aws_sdk_appstream.types.shared_image_permissions

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appstream.types.shared_image_permissions.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SharedImagePermissionsList:
    import aws_sdk_appstream.types.shared_image_permissions

    out: SharedImagePermissionsList = []
    for item in data:
        out.append(
            aws_sdk_appstream.types.shared_image_permissions.deserialize_aws_json_1_1(
                item
            )
        )
    return out
