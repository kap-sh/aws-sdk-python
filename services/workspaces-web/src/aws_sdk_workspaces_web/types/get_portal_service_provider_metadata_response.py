"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetPortalServiceProviderMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.saml_metadata


class GetPortalServiceProviderMetadataResponse(TypedDict, closed=True):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    service_provider_saml_metadata: NotRequired[
        "aws_sdk_workspaces_web.types.saml_metadata.SamlMetadata"
    ]
    """<p>The service provider SAML metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPortalServiceProviderMetadataResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    if "service_provider_saml_metadata" in value:
        out["serviceProviderSamlMetadata"] = value["service_provider_saml_metadata"]
    return out


def deserialize_json(data: dict) -> GetPortalServiceProviderMetadataResponse:
    out: GetPortalServiceProviderMetadataResponse = {}  # type: ignore[typeddict-item]
    if "portalArn" in data:
        out["portal_arn"] = data["portalArn"]
    else:
        raise DeserializationError(
            "GetPortalServiceProviderMetadataResponse.portal_arn required"
        )
    if "serviceProviderSamlMetadata" in data:
        out["service_provider_saml_metadata"] = data["serviceProviderSamlMetadata"]
    return out
