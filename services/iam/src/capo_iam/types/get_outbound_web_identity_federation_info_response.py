"""Generated from Smithy shape ``com.amazonaws.iam#GetOutboundWebIdentityFederationInfoResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.string_type


class GetOutboundWebIdentityFederationInfoResponse(TypedDict, closed=True):
    issuer_identifier: NotRequired["capo_iam.types.string_type.stringType"]
    """<p>A unique issuer URL for your Amazon Web Services account that hosts the OpenID Connect (OIDC) discovery endpoints at <code>/.well-known/openid-configuration and /.well-known/jwks.json</code>. The OpenID Connect (OIDC) discovery endpoints contain verification keys and metadata necessary for token verification.</p>"""
    jwt_vending_enabled: "capo_iam.types.boolean_type.booleanType"
    """<p>Indicates whether outbound identity federation is currently enabled for your Amazon Web Services account. When true, IAM principals in the account can call the <code>GetWebIdentityToken</code> API to obtain JSON Web Tokens (JWTs) for authentication with external services. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetOutboundWebIdentityFederationInfoResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "issuer_identifier" in value:
        pairs.append((f"{prefix}.IssuerIdentifier", str(value["issuer_identifier"])))
    pairs.append(
        (
            f"{prefix}.JwtVendingEnabled",
            "true" if value.get("jwt_vending_enabled", False) else "false",
        )
    )


def deserialize_query(el: Element) -> GetOutboundWebIdentityFederationInfoResponse:
    out: GetOutboundWebIdentityFederationInfoResponse = {}  # type: ignore[typeddict-item]
    child_issuer_identifier = el.find("IssuerIdentifier")
    if child_issuer_identifier is not None:
        out["issuer_identifier"] = str(child_issuer_identifier.text or "")
    child_jwt_vending_enabled = el.find("JwtVendingEnabled")
    if child_jwt_vending_enabled is not None:
        out["jwt_vending_enabled"] = (
            child_jwt_vending_enabled.text or ""
        ).lower() == "true"
    else:
        out["jwt_vending_enabled"] = False
    return out
