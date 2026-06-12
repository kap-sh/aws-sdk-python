"""Generated from Smithy shape ``com.amazonaws.opensearch#SAMLOptionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.integer_class
    import aws_sdk_opensearch.types.saml_idp
    import aws_sdk_opensearch.types.string


class SAMLOptionsOutput(TypedDict):
    enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>True if SAML is enabled.</p>"""
    idp: NotRequired["aws_sdk_opensearch.types.saml_idp.SAMLIdp"]
    """<p>Describes the SAML identity provider's information.</p>"""
    subject_key: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The key used for matching the SAML subject attribute.</p>"""
    roles_key: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>The key used for matching the SAML roles attribute.</p>"""
    session_timeout_minutes: NotRequired[
        "aws_sdk_opensearch.types.integer_class.IntegerClass"
    ]
    """<p>The duration, in minutes, after which a user session becomes inactive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAMLOptionsOutput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "idp" in value:
        import aws_sdk_opensearch.types.saml_idp

        out["Idp"] = aws_sdk_opensearch.types.saml_idp.serialize_json(value["idp"])
    if "subject_key" in value:
        out["SubjectKey"] = value["subject_key"]
    if "roles_key" in value:
        out["RolesKey"] = value["roles_key"]
    if "session_timeout_minutes" in value:
        out["SessionTimeoutMinutes"] = value["session_timeout_minutes"]
    return out


def deserialize_json(data: dict) -> SAMLOptionsOutput:
    out: SAMLOptionsOutput = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "Idp" in data:
        import aws_sdk_opensearch.types.saml_idp

        out["idp"] = aws_sdk_opensearch.types.saml_idp.deserialize_json(data["Idp"])
    if "SubjectKey" in data:
        out["subject_key"] = data["SubjectKey"]
    if "RolesKey" in data:
        out["roles_key"] = data["RolesKey"]
    if "SessionTimeoutMinutes" in data:
        out["session_timeout_minutes"] = data["SessionTimeoutMinutes"]
    return out
