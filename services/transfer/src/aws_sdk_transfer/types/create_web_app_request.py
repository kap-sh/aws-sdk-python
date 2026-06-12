"""Generated from Smithy shape ``com.amazonaws.transfer#CreateWebAppRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.tags
    import aws_sdk_transfer.types.web_app_access_endpoint
    import aws_sdk_transfer.types.web_app_endpoint_details
    import aws_sdk_transfer.types.web_app_endpoint_policy
    import aws_sdk_transfer.types.web_app_identity_provider_details
    import aws_sdk_transfer.types.web_app_units


class CreateWebAppRequest(TypedDict):
    identity_provider_details: "aws_sdk_transfer.types.web_app_identity_provider_details.WebAppIdentityProviderDetails"
    """<p>You can provide a structure that contains the details for the identity provider to use with your web app.</p> <p>For more details about this parameter, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/webapp-identity-center.html\">Configure your identity provider for Transfer Family web apps</a>.</p>"""
    access_endpoint: NotRequired[
        "aws_sdk_transfer.types.web_app_access_endpoint.WebAppAccessEndpoint"
    ]
    """<p>The <code>AccessEndpoint</code> is the URL that you provide to your users for them to interact with the Transfer Family web app. You can specify a custom URL or use the default value.</p> <p>Before you enter a custom URL for this parameter, follow the steps described in <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/webapp-customize.html\">Update your access endpoint with a custom URL</a>.</p>"""
    web_app_units: NotRequired["aws_sdk_transfer.types.web_app_units.WebAppUnits"]
    """<p>A union that contains the value for number of concurrent connections or the user sessions on your web app.</p>"""
    tags: NotRequired["aws_sdk_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for web apps.</p>"""
    web_app_endpoint_policy: NotRequired[
        "aws_sdk_transfer.types.web_app_endpoint_policy.WebAppEndpointPolicy"
    ]
    """<p> Setting for the type of endpoint policy for the web app. The default value is <code>STANDARD</code>. </p> <p>If you are creating the web app in an Amazon Web Services GovCloud (US) Region, you can set this parameter to <code>FIPS</code>.</p>"""
    endpoint_details: NotRequired[
        "aws_sdk_transfer.types.web_app_endpoint_details.WebAppEndpointDetails"
    ]
    """<p>The endpoint configuration for the web app. You can specify whether the web app endpoint is publicly accessible or hosted within a VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWebAppRequest) -> dict:
    out: dict = {}
    import aws_sdk_transfer.types.web_app_identity_provider_details

    out["IdentityProviderDetails"] = (
        aws_sdk_transfer.types.web_app_identity_provider_details.serialize_aws_json_1_1(
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
    if "tags" in value:
        import aws_sdk_transfer.types.tags

        out["Tags"] = aws_sdk_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    if "web_app_endpoint_policy" in value:
        import aws_sdk_transfer.types.web_app_endpoint_policy

        out["WebAppEndpointPolicy"] = (
            aws_sdk_transfer.types.web_app_endpoint_policy.serialize_aws_json_1_1(
                value["web_app_endpoint_policy"]
            )
        )
    if "endpoint_details" in value:
        import aws_sdk_transfer.types.web_app_endpoint_details

        out["EndpointDetails"] = (
            aws_sdk_transfer.types.web_app_endpoint_details.serialize_aws_json_1_1(
                value["endpoint_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWebAppRequest:
    out: CreateWebAppRequest = {}  # type: ignore[typeddict-item]
    if "IdentityProviderDetails" in data:
        import aws_sdk_transfer.types.web_app_identity_provider_details

        out["identity_provider_details"] = (
            aws_sdk_transfer.types.web_app_identity_provider_details.deserialize_aws_json_1_1(
                data["IdentityProviderDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreateWebAppRequest.identity_provider_details required"
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
    if "Tags" in data:
        import aws_sdk_transfer.types.tags

        out["tags"] = aws_sdk_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "WebAppEndpointPolicy" in data:
        import aws_sdk_transfer.types.web_app_endpoint_policy

        out["web_app_endpoint_policy"] = (
            aws_sdk_transfer.types.web_app_endpoint_policy.deserialize_aws_json_1_1(
                data["WebAppEndpointPolicy"]
            )
        )
    if "EndpointDetails" in data:
        import aws_sdk_transfer.types.web_app_endpoint_details

        out["endpoint_details"] = (
            aws_sdk_transfer.types.web_app_endpoint_details.deserialize_aws_json_1_1(
                data["EndpointDetails"]
            )
        )
    return out
