"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#DeleteLicenseServerEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint


class DeleteLicenseServerEndpointResponse(TypedDict):
    license_server_endpoint: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint.LicenseServerEndpoint"
    ]
    """<p>Shows details from the <code>LicenseServerEndpoint</code> resource that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLicenseServerEndpointResponse) -> dict:
    out: dict = {}
    if "license_server_endpoint" in value:
        import aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint

        out["LicenseServerEndpoint"] = (
            aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint.serialize_json(
                value["license_server_endpoint"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteLicenseServerEndpointResponse:
    out: DeleteLicenseServerEndpointResponse = {}  # type: ignore[typeddict-item]
    if "LicenseServerEndpoint" in data:
        import aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint

        out["license_server_endpoint"] = (
            aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint.deserialize_json(
                data["LicenseServerEndpoint"]
            )
        )
    return out
