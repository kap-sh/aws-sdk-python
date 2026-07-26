"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#DeleteLicenseServerEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.arn
    import capo_license_manager_user_subscriptions.types.server_type


class DeleteLicenseServerEndpointRequest(TypedDict, closed=True):
    license_server_endpoint_arn: "capo_license_manager_user_subscriptions.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the <code>LicenseServerEndpoint</code> resource to delete.</p>"""
    server_type: "capo_license_manager_user_subscriptions.types.server_type.ServerType"
    """<p>The type of License Server that the delete request refers to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLicenseServerEndpointRequest) -> dict:
    out: dict = {}
    out["LicenseServerEndpointArn"] = value["license_server_endpoint_arn"]
    out["ServerType"] = value["server_type"]
    return out


def deserialize_json(data: dict) -> DeleteLicenseServerEndpointRequest:
    out: DeleteLicenseServerEndpointRequest = {}  # type: ignore[typeddict-item]
    if "LicenseServerEndpointArn" in data:
        out["license_server_endpoint_arn"] = data["LicenseServerEndpointArn"]
    else:
        raise DeserializationError(
            "DeleteLicenseServerEndpointRequest.license_server_endpoint_arn required"
        )
    if "ServerType" in data:
        out["server_type"] = data["ServerType"]
    else:
        raise DeserializationError(
            "DeleteLicenseServerEndpointRequest.server_type required"
        )
    return out
