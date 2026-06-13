"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#LicenseServerEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint

LicenseServerEndpointList: TypeAlias = list[
    "aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint.LicenseServerEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: LicenseServerEndpointList) -> list:
    import aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LicenseServerEndpointList:
    import aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint

    out: LicenseServerEndpointList = []
    for item in data:
        out.append(
            aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint.deserialize_json(
                item
            )
        )
    return out
