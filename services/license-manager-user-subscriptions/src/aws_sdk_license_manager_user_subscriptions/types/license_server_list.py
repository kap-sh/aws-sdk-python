"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#LicenseServerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.license_server

LicenseServerList: TypeAlias = list[
    "aws_sdk_license_manager_user_subscriptions.types.license_server.LicenseServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: LicenseServerList) -> list:
    import aws_sdk_license_manager_user_subscriptions.types.license_server

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager_user_subscriptions.types.license_server.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LicenseServerList:
    import aws_sdk_license_manager_user_subscriptions.types.license_server

    out: LicenseServerList = []
    for item in data:
        out.append(
            aws_sdk_license_manager_user_subscriptions.types.license_server.deserialize_json(
                item
            )
        )
    return out
