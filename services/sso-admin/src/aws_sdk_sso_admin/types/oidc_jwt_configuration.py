"""Generated from Smithy shape ``com.amazonaws.ssoadmin#OidcJwtConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.claim_attribute_path
    import aws_sdk_sso_admin.types.jmes_path
    import aws_sdk_sso_admin.types.jwks_retrieval_option
    import aws_sdk_sso_admin.types.trusted_token_issuer_url


class OidcJwtConfiguration(TypedDict, closed=True):
    issuer_url: "aws_sdk_sso_admin.types.trusted_token_issuer_url.TrustedTokenIssuerUrl"
    """<p>The URL that IAM Identity Center uses for OpenID Discovery. OpenID Discovery is used to obtain the information required to verify the tokens that the trusted token issuer generates.</p>"""
    claim_attribute_path: (
        "aws_sdk_sso_admin.types.claim_attribute_path.ClaimAttributePath"
    )
    """<p>The path of the source attribute in the JWT from the trusted token issuer. The attribute mapped by this JMESPath expression is compared against the attribute mapped by <code>IdentityStoreAttributePath</code> when a trusted token issuer token is exchanged for an IAM Identity Center token.</p>"""
    identity_store_attribute_path: "aws_sdk_sso_admin.types.jmes_path.JMESPath"
    """<p>The path of the destination attribute in a JWT from IAM Identity Center. The attribute mapped by this JMESPath expression is compared against the attribute mapped by <code>ClaimAttributePath</code> when a trusted token issuer token is exchanged for an IAM Identity Center token. </p>"""
    jwks_retrieval_option: (
        "aws_sdk_sso_admin.types.jwks_retrieval_option.JwksRetrievalOption"
    )
    """<p>The method that the trusted token issuer can use to retrieve the JSON Web Key Set used to verify a JWT.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OidcJwtConfiguration) -> dict:
    out: dict = {}
    out["IssuerUrl"] = value["issuer_url"]
    out["ClaimAttributePath"] = value["claim_attribute_path"]
    out["IdentityStoreAttributePath"] = value["identity_store_attribute_path"]
    import aws_sdk_sso_admin.types.jwks_retrieval_option

    out["JwksRetrievalOption"] = (
        aws_sdk_sso_admin.types.jwks_retrieval_option.serialize_aws_json_1_1(
            value["jwks_retrieval_option"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OidcJwtConfiguration:
    out: OidcJwtConfiguration = {}  # type: ignore[typeddict-item]
    if "IssuerUrl" in data:
        out["issuer_url"] = data["IssuerUrl"]
    else:
        raise DeserializationError("OidcJwtConfiguration.issuer_url required")
    if "ClaimAttributePath" in data:
        out["claim_attribute_path"] = data["ClaimAttributePath"]
    else:
        raise DeserializationError("OidcJwtConfiguration.claim_attribute_path required")
    if "IdentityStoreAttributePath" in data:
        out["identity_store_attribute_path"] = data["IdentityStoreAttributePath"]
    else:
        raise DeserializationError(
            "OidcJwtConfiguration.identity_store_attribute_path required"
        )
    if "JwksRetrievalOption" in data:
        import aws_sdk_sso_admin.types.jwks_retrieval_option

        out["jwks_retrieval_option"] = (
            aws_sdk_sso_admin.types.jwks_retrieval_option.deserialize_aws_json_1_1(
                data["JwksRetrievalOption"]
            )
        )
    else:
        raise DeserializationError(
            "OidcJwtConfiguration.jwks_retrieval_option required"
        )
    return out
