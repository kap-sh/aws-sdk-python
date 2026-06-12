"""Generated from Smithy shape ``com.amazonaws.finspacedata#ApplicationPermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.application_permission

ApplicationPermissionList: TypeAlias = list[
    "aws_sdk_finspace_data.types.application_permission.ApplicationPermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationPermissionList) -> list:
    import aws_sdk_finspace_data.types.application_permission

    out: list = []
    for item in value:
        out.append(
            aws_sdk_finspace_data.types.application_permission.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ApplicationPermissionList:
    import aws_sdk_finspace_data.types.application_permission

    out: ApplicationPermissionList = []
    for item in data:
        out.append(
            aws_sdk_finspace_data.types.application_permission.deserialize_json(item)
        )
    return out
