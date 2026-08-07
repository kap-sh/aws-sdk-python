"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#JwtValidationActionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims
    import capo_elastic_load_balancing_v2.types.jwt_validation_action_issuer
    import capo_elastic_load_balancing_v2.types.jwt_validation_action_jwks_endpoint


class JwtValidationActionConfig(TypedDict, closed=True):
    jwks_endpoint: NotRequired[
        "capo_elastic_load_balancing_v2.types.jwt_validation_action_jwks_endpoint.JwtValidationActionJwksEndpoint"
    ]
    """<p>The JSON Web Key Set (JWKS) endpoint. This endpoint contains JSON Web Keys (JWK) that are used to validate signatures from the provider.</p> <p>This must be a full URL, including the HTTPS protocol, the domain, and the path. The maximum length is 256 characters.</p>"""
    issuer: NotRequired[
        "capo_elastic_load_balancing_v2.types.jwt_validation_action_issuer.JwtValidationActionIssuer"
    ]
    """<p>The issuer of the JWT. The maximum length is 256 characters.</p>"""
    additional_claims: NotRequired[
        "capo_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims.JwtValidationActionAdditionalClaims"
    ]
    """<p>Additional claims to validate. The maximum size of the list is 10. We validate the <code>exp</code>, <code>iss</code>, <code>nbf</code>, and <code>iat</code> claims by default.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: JwtValidationActionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "jwks_endpoint" in value:
        pairs.append((f"{key_prefix}JwksEndpoint", str(value["jwks_endpoint"])))
    if "issuer" in value:
        pairs.append((f"{key_prefix}Issuer", str(value["issuer"])))
    if "additional_claims" in value:
        import capo_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims

        capo_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims.serialize_query(
            value["additional_claims"], pairs, f"{key_prefix}AdditionalClaims"
        )


def deserialize_query(el: Element) -> JwtValidationActionConfig:
    out: JwtValidationActionConfig = {}  # type: ignore[typeddict-item]
    child_jwks_endpoint = el.find("JwksEndpoint")
    if child_jwks_endpoint is not None:
        out["jwks_endpoint"] = str(child_jwks_endpoint.text or "")
    child_issuer = el.find("Issuer")
    if child_issuer is not None:
        out["issuer"] = str(child_issuer.text or "")
    child_additional_claims = el.find("AdditionalClaims")
    if child_additional_claims is not None:
        import capo_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims

        out["additional_claims"] = (
            capo_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims.deserialize_query(
                child_additional_claims
            )
        )
    return out
