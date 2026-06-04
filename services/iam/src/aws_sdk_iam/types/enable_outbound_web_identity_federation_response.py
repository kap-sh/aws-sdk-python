"""Generated from Smithy shape ``com.amazonaws.iam#EnableOutboundWebIdentityFederationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.string_type


class EnableOutboundWebIdentityFederationResponse(TypedDict):
    issuer_identifier: NotRequired["aws_sdk_iam.types.string_type.stringType"]
    """<p>A unique issuer URL for your Amazon Web Services account that hosts the OpenID Connect (OIDC) discovery endpoints at <code>/.well-known/openid-configuration and /.well-known/jwks.json</code>. The OpenID Connect (OIDC) discovery endpoints contain verification keys and metadata necessary for token verification.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnableOutboundWebIdentityFederationResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "issuer_identifier" in value:
        pairs.append((f"{prefix}.IssuerIdentifier", str(value["issuer_identifier"])))


def deserialize_query(el: Element) -> EnableOutboundWebIdentityFederationResponse:
    out: EnableOutboundWebIdentityFederationResponse = {}  # type: ignore[typeddict-item]
    child_issuer_identifier = el.find("IssuerIdentifier")
    if child_issuer_identifier is not None:
        out["issuer_identifier"] = str(child_issuer_identifier.text or "")
    return out
