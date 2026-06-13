"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListLicenseServerEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint_list


class ListLicenseServerEndpointsResponse(TypedDict):
    license_server_endpoints: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint_list.LicenseServerEndpointList"
    ]
    """<p>An array of <code>LicenseServerEndpoint</code> resources that contain detailed information about the RDS License Servers that meet the request criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLicenseServerEndpointsResponse) -> dict:
    out: dict = {}
    if "license_server_endpoints" in value:
        import aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint_list

        out["LicenseServerEndpoints"] = (
            aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint_list.serialize_json(
                value["license_server_endpoints"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLicenseServerEndpointsResponse:
    out: ListLicenseServerEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "LicenseServerEndpoints" in data:
        import aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint_list

        out["license_server_endpoints"] = (
            aws_sdk_license_manager_user_subscriptions.types.license_server_endpoint_list.deserialize_json(
                data["LicenseServerEndpoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
