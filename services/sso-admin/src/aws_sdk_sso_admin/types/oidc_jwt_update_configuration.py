"""Generated from Smithy shape ``com.amazonaws.ssoadmin#OidcJwtUpdateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.claim_attribute_path
    import aws_sdk_sso_admin.types.jmes_path
    import aws_sdk_sso_admin.types.jwks_retrieval_option


class OidcJwtUpdateConfiguration(TypedDict, closed=True):
    claim_attribute_path: NotRequired[
        "aws_sdk_sso_admin.types.claim_attribute_path.ClaimAttributePath"
    ]
    """<p>The path of the source attribute in the JWT from the trusted token issuer. The attribute mapped by this JMESPath expression is compared against the attribute mapped by <code>IdentityStoreAttributePath</code> when a trusted token issuer token is exchanged for an IAM Identity Center token.</p>"""
    identity_store_attribute_path: NotRequired[
        "aws_sdk_sso_admin.types.jmes_path.JMESPath"
    ]
    """<p>The path of the destination attribute in a JWT from IAM Identity Center. The attribute mapped by this JMESPath expression is compared against the attribute mapped by <code>ClaimAttributePath</code> when a trusted token issuer token is exchanged for an IAM Identity Center token.</p>"""
    jwks_retrieval_option: NotRequired[
        "aws_sdk_sso_admin.types.jwks_retrieval_option.JwksRetrievalOption"
    ]
    """<p>The method that the trusted token issuer can use to retrieve the JSON Web Key Set used to verify a JWT.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OidcJwtUpdateConfiguration) -> dict:
    out: dict = {}
    if "claim_attribute_path" in value:
        out["ClaimAttributePath"] = value["claim_attribute_path"]
    if "identity_store_attribute_path" in value:
        out["IdentityStoreAttributePath"] = value["identity_store_attribute_path"]
    if "jwks_retrieval_option" in value:
        import aws_sdk_sso_admin.types.jwks_retrieval_option

        out["JwksRetrievalOption"] = (
            aws_sdk_sso_admin.types.jwks_retrieval_option.serialize_aws_json_1_1(
                value["jwks_retrieval_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OidcJwtUpdateConfiguration:
    out: OidcJwtUpdateConfiguration = {}  # type: ignore[typeddict-item]
    if "ClaimAttributePath" in data:
        out["claim_attribute_path"] = data["ClaimAttributePath"]
    if "IdentityStoreAttributePath" in data:
        out["identity_store_attribute_path"] = data["IdentityStoreAttributePath"]
    if "JwksRetrievalOption" in data:
        import aws_sdk_sso_admin.types.jwks_retrieval_option

        out["jwks_retrieval_option"] = (
            aws_sdk_sso_admin.types.jwks_retrieval_option.deserialize_aws_json_1_1(
                data["JwksRetrievalOption"]
            )
        )
    return out
