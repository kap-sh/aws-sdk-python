"""Generated from Smithy shape ``com.amazonaws.opensearch#JWTOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.jwks_url
    import aws_sdk_opensearch.types.roles_key
    import aws_sdk_opensearch.types.string
    import aws_sdk_opensearch.types.subject_key


class JWTOptionsInput(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>True to enable JWT authentication and authorization for a domain.</p>"""
    subject_key: NotRequired["aws_sdk_opensearch.types.subject_key.SubjectKey"]
    """<p>Element of the JWT assertion to use for the user name.</p>"""
    roles_key: NotRequired["aws_sdk_opensearch.types.roles_key.RolesKey"]
    """<p>Element of the JWT assertion to use for roles.</p>"""
    jwks_url: NotRequired["aws_sdk_opensearch.types.jwks_url.JwksUrl"]
    """<p>The URL endpoint that hosts the JSON Web Key Set (JWKS) containing public keys used to verify JWT signatures.</p>"""
    public_key: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>Element of the JWT assertion used by the cluster to verify JWT signatures.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JWTOptionsInput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "subject_key" in value:
        out["SubjectKey"] = value["subject_key"]
    if "roles_key" in value:
        out["RolesKey"] = value["roles_key"]
    if "jwks_url" in value:
        out["JwksUrl"] = value["jwks_url"]
    if "public_key" in value:
        out["PublicKey"] = value["public_key"]
    return out


def deserialize_json(data: dict) -> JWTOptionsInput:
    out: JWTOptionsInput = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "SubjectKey" in data:
        out["subject_key"] = data["SubjectKey"]
    if "RolesKey" in data:
        out["roles_key"] = data["RolesKey"]
    if "JwksUrl" in data:
        out["jwks_url"] = data["JwksUrl"]
    if "PublicKey" in data:
        out["public_key"] = data["PublicKey"]
    return out
