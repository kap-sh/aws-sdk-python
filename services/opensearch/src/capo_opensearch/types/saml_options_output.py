"""Generated from Smithy shape ``com.amazonaws.opensearch#SAMLOptionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.integer_class
    import capo_opensearch.types.saml_idp
    import capo_opensearch.types.string


class SAMLOptionsOutput(TypedDict, closed=True):
    enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>True if SAML is enabled.</p>"""
    idp: NotRequired["capo_opensearch.types.saml_idp.SAMLIdp"]
    """<p>Describes the SAML identity provider's information.</p>"""
    subject_key: NotRequired["capo_opensearch.types.string.String"]
    """<p>The key used for matching the SAML subject attribute.</p>"""
    roles_key: NotRequired["capo_opensearch.types.string.String"]
    """<p>The key used for matching the SAML roles attribute.</p>"""
    session_timeout_minutes: NotRequired[
        "capo_opensearch.types.integer_class.IntegerClass"
    ]
    """<p>The duration, in minutes, after which a user session becomes inactive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAMLOptionsOutput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "idp" in value:
        import capo_opensearch.types.saml_idp

        out["Idp"] = capo_opensearch.types.saml_idp.serialize_json(value["idp"])
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
        import capo_opensearch.types.saml_idp

        out["idp"] = capo_opensearch.types.saml_idp.deserialize_json(data["Idp"])
    if "SubjectKey" in data:
        out["subject_key"] = data["SubjectKey"]
    if "RolesKey" in data:
        out["roles_key"] = data["RolesKey"]
    if "SessionTimeoutMinutes" in data:
        out["session_timeout_minutes"] = data["SessionTimeoutMinutes"]
    return out
