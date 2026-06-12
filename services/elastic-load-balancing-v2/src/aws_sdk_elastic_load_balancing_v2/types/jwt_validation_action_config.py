"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#JwtValidationActionConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_issuer
    import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_jwks_endpoint


class JwtValidationActionConfig(TypedDict):
    jwks_endpoint: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_jwks_endpoint.JwtValidationActionJwksEndpoint"
    ]
    """<p>The JSON Web Key Set (JWKS) endpoint. This endpoint contains JSON Web Keys (JWK) that are used to validate signatures from the provider.</p> <p>This must be a full URL, including the HTTPS protocol, the domain, and the path. The maximum length is 256 characters.</p>"""
    issuer: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_issuer.JwtValidationActionIssuer"
    ]
    """<p>The issuer of the JWT. The maximum length is 256 characters.</p>"""
    additional_claims: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims.JwtValidationActionAdditionalClaims"
    ]
    """<p>Additional claims to validate. The maximum size of the list is 10. We validate the <code>exp</code>, <code>iss</code>, <code>nbf</code>, and <code>iat</code> claims by default.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: JwtValidationActionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "jwks_endpoint" in value:
        pairs.append((f"{prefix}.JwksEndpoint", str(value["jwks_endpoint"])))
    if "issuer" in value:
        pairs.append((f"{prefix}.Issuer", str(value["issuer"])))
    if "additional_claims" in value:
        import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims

        aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims.serialize_query(
            value["additional_claims"], pairs, f"{prefix}.AdditionalClaims"
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
        import aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims

        out["additional_claims"] = (
            aws_sdk_elastic_load_balancing_v2.types.jwt_validation_action_additional_claims.deserialize_query(
                child_additional_claims
            )
        )
    return out
