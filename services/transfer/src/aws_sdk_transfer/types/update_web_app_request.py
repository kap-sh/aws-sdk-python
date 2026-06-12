"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateWebAppRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.update_web_app_endpoint_details
    import aws_sdk_transfer.types.update_web_app_identity_provider_details
    import aws_sdk_transfer.types.web_app_access_endpoint
    import aws_sdk_transfer.types.web_app_id
    import aws_sdk_transfer.types.web_app_units


class UpdateWebAppRequest(TypedDict):
    web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId"
    """<p>Provide the identifier of the web app that you are updating.</p>"""
    identity_provider_details: NotRequired[
        "aws_sdk_transfer.types.update_web_app_identity_provider_details.UpdateWebAppIdentityProviderDetails"
    ]
    """<p>Provide updated identity provider values in a <code>WebAppIdentityProviderDetails</code> object.</p>"""
    access_endpoint: NotRequired[
        "aws_sdk_transfer.types.web_app_access_endpoint.WebAppAccessEndpoint"
    ]
    """<p>The <code>AccessEndpoint</code> is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.</p>"""
    web_app_units: NotRequired["aws_sdk_transfer.types.web_app_units.WebAppUnits"]
    """<p>A union that contains the value for number of concurrent connections or the user sessions on your web app.</p>"""
    endpoint_details: NotRequired[
        "aws_sdk_transfer.types.update_web_app_endpoint_details.UpdateWebAppEndpointDetails"
    ]
    """<p>The updated endpoint configuration for the web app. You can modify the endpoint type and VPC configuration settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebAppRequest) -> dict:
    out: dict = {}
    out["WebAppId"] = value["web_app_id"]
    if "identity_provider_details" in value:
        import aws_sdk_transfer.types.update_web_app_identity_provider_details

        out["IdentityProviderDetails"] = (
            aws_sdk_transfer.types.update_web_app_identity_provider_details.serialize_aws_json_1_1(
                value["identity_provider_details"]
            )
        )
    if "access_endpoint" in value:
        out["AccessEndpoint"] = value["access_endpoint"]
    if "web_app_units" in value:
        import aws_sdk_transfer.types.web_app_units

        out["WebAppUnits"] = (
            aws_sdk_transfer.types.web_app_units.serialize_aws_json_1_1(
                value["web_app_units"]
            )
        )
    if "endpoint_details" in value:
        import aws_sdk_transfer.types.update_web_app_endpoint_details

        out["EndpointDetails"] = (
            aws_sdk_transfer.types.update_web_app_endpoint_details.serialize_aws_json_1_1(
                value["endpoint_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWebAppRequest:
    out: UpdateWebAppRequest = {}  # type: ignore[typeddict-item]
    if "WebAppId" in data:
        out["web_app_id"] = data["WebAppId"]
    else:
        raise DeserializationError("UpdateWebAppRequest.web_app_id required")
    if "IdentityProviderDetails" in data:
        import aws_sdk_transfer.types.update_web_app_identity_provider_details

        out["identity_provider_details"] = (
            aws_sdk_transfer.types.update_web_app_identity_provider_details.deserialize_aws_json_1_1(
                data["IdentityProviderDetails"]
            )
        )
    if "AccessEndpoint" in data:
        out["access_endpoint"] = data["AccessEndpoint"]
    if "WebAppUnits" in data:
        import aws_sdk_transfer.types.web_app_units

        out["web_app_units"] = (
            aws_sdk_transfer.types.web_app_units.deserialize_aws_json_1_1(
                data["WebAppUnits"]
            )
        )
    if "EndpointDetails" in data:
        import aws_sdk_transfer.types.update_web_app_endpoint_details

        out["endpoint_details"] = (
            aws_sdk_transfer.types.update_web_app_endpoint_details.deserialize_aws_json_1_1(
                data["EndpointDetails"]
            )
        )
    return out
