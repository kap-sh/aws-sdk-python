"""Generated from Smithy shape ``com.amazonaws.finspace#FederationParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.attribute_map
    import aws_sdk_finspace.types.federation_provider_name
    import aws_sdk_finspace.types.saml_metadata_document
    import aws_sdk_finspace.types.url
    import aws_sdk_finspace.types.urn


class FederationParameters(TypedDict):
    saml_metadata_document: NotRequired[
        "aws_sdk_finspace.types.saml_metadata_document.SamlMetadataDocument"
    ]
    """<p>SAML 2.0 Metadata document from identity provider (IdP).</p>"""
    saml_metadata_url: NotRequired["aws_sdk_finspace.types.url.url"]
    """<p>Provide the metadata URL from your SAML 2.0 compliant identity provider (IdP).</p>"""
    application_call_back_url: NotRequired["aws_sdk_finspace.types.url.url"]
    """<p>The redirect or sign-in URL that should be entered into the SAML 2.0 compliant identity provider configuration (IdP).</p>"""
    federation_urn: NotRequired["aws_sdk_finspace.types.urn.urn"]
    """<p>The Uniform Resource Name (URN). Also referred as Service Provider URN or Audience URI or Service Provider Entity ID.</p>"""
    federation_provider_name: NotRequired[
        "aws_sdk_finspace.types.federation_provider_name.FederationProviderName"
    ]
    """<p>Name of the identity provider (IdP).</p>"""
    attribute_map: NotRequired["aws_sdk_finspace.types.attribute_map.AttributeMap"]
    """<p>SAML attribute name and value. The name must always be <code>Email</code> and the value should be set to the attribute definition in which user email is set. For example, name would be <code>Email</code> and value <code>http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress</code>. Please check your SAML 2.0 compliant identity provider (IdP) documentation for details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FederationParameters) -> dict:
    out: dict = {}
    if "saml_metadata_document" in value:
        out["samlMetadataDocument"] = value["saml_metadata_document"]
    if "saml_metadata_url" in value:
        out["samlMetadataURL"] = value["saml_metadata_url"]
    if "application_call_back_url" in value:
        out["applicationCallBackURL"] = value["application_call_back_url"]
    if "federation_urn" in value:
        out["federationURN"] = value["federation_urn"]
    if "federation_provider_name" in value:
        out["federationProviderName"] = value["federation_provider_name"]
    if "attribute_map" in value:
        import aws_sdk_finspace.types.attribute_map

        out["attributeMap"] = aws_sdk_finspace.types.attribute_map.serialize_json(
            value["attribute_map"]
        )
    return out


def deserialize_json(data: dict) -> FederationParameters:
    out: FederationParameters = {}  # type: ignore[typeddict-item]
    if "samlMetadataDocument" in data:
        out["saml_metadata_document"] = data["samlMetadataDocument"]
    if "samlMetadataURL" in data:
        out["saml_metadata_url"] = data["samlMetadataURL"]
    if "applicationCallBackURL" in data:
        out["application_call_back_url"] = data["applicationCallBackURL"]
    if "federationURN" in data:
        out["federation_urn"] = data["federationURN"]
    if "federationProviderName" in data:
        out["federation_provider_name"] = data["federationProviderName"]
    if "attributeMap" in data:
        import aws_sdk_finspace.types.attribute_map

        out["attribute_map"] = aws_sdk_finspace.types.attribute_map.deserialize_json(
            data["attributeMap"]
        )
    return out
