"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceAdminList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_admin_summary

AppInstanceAdminList: TypeAlias = list[
    "aws_sdk_chime_sdk_identity.types.app_instance_admin_summary.AppInstanceAdminSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceAdminList) -> list:
    import aws_sdk_chime_sdk_identity.types.app_instance_admin_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_identity.types.app_instance_admin_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AppInstanceAdminList:
    import aws_sdk_chime_sdk_identity.types.app_instance_admin_summary

    out: AppInstanceAdminList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_identity.types.app_instance_admin_summary.deserialize_json(
                item
            )
        )
    return out
