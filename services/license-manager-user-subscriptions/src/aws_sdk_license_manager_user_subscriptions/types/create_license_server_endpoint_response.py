"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#CreateLicenseServerEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.arn

class CreateLicenseServerEndpointResponse(TypedDict):
    identity_provider_arn: NotRequired["aws_sdk_license_manager_user_subscriptions.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the identity provider specified in the request.</p>"""
    license_server_endpoint_arn: NotRequired["aws_sdk_license_manager_user_subscriptions.types.arn.Arn"]
    """<p>The ARN of the <code>LicenseServerEndpoint</code> resource.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateLicenseServerEndpointResponse) -> dict:
    out: dict = {}
    if "identity_provider_arn" in value:
        out["IdentityProviderArn"] = value["identity_provider_arn"]
    if "license_server_endpoint_arn" in value:
        out["LicenseServerEndpointArn"] = value["license_server_endpoint_arn"]
    return out


def deserialize_json(data: dict) -> CreateLicenseServerEndpointResponse:
    out: CreateLicenseServerEndpointResponse = {}  # type: ignore[typeddict-item]
    if "IdentityProviderArn" in data:
        out["identity_provider_arn"] = data["IdentityProviderArn"]
    if "LicenseServerEndpointArn" in data:
        out["license_server_endpoint_arn"] = data["LicenseServerEndpointArn"]
    return out