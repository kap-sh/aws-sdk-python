"""Generated from Smithy shape ``com.amazonaws.opensearch#SAMLOptionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.backend_role
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.integer_class
    import aws_sdk_opensearch.types.saml_idp
    import aws_sdk_opensearch.types.string
    import aws_sdk_opensearch.types.username


class SAMLOptionsInput(TypedDict):
    enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>True to enable SAML authentication for a domain.</p>"""
    idp: NotRequired["aws_sdk_opensearch.types.saml_idp.SAMLIdp"]
    """<p>The SAML Identity Provider's information.</p>"""
    master_user_name: NotRequired["aws_sdk_opensearch.types.username.Username"]
    """<p>The SAML master user name, which is stored in the domain's internal user database.</p>"""
    master_backend_role: NotRequired[
        "aws_sdk_opensearch.types.backend_role.BackendRole"
    ]
    """<p>The backend role that the SAML master user is mapped to.</p>"""
    subject_key: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>Element of the SAML assertion to use for the user name. Default is <code>NameID</code>.</p>"""
    roles_key: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>Element of the SAML assertion to use for backend roles. Default is <code>roles</code>.</p>"""
    session_timeout_minutes: NotRequired[
        "aws_sdk_opensearch.types.integer_class.IntegerClass"
    ]
    """<p>The duration, in minutes, after which a user session becomes inactive. Acceptable values are between 1 and 1440, and the default value is 60.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAMLOptionsInput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "idp" in value:
        import aws_sdk_opensearch.types.saml_idp

        out["Idp"] = aws_sdk_opensearch.types.saml_idp.serialize_json(value["idp"])
    if "master_user_name" in value:
        out["MasterUserName"] = value["master_user_name"]
    if "master_backend_role" in value:
        out["MasterBackendRole"] = value["master_backend_role"]
    if "subject_key" in value:
        out["SubjectKey"] = value["subject_key"]
    if "roles_key" in value:
        out["RolesKey"] = value["roles_key"]
    if "session_timeout_minutes" in value:
        out["SessionTimeoutMinutes"] = value["session_timeout_minutes"]
    return out


def deserialize_json(data: dict) -> SAMLOptionsInput:
    out: SAMLOptionsInput = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "Idp" in data:
        import aws_sdk_opensearch.types.saml_idp

        out["idp"] = aws_sdk_opensearch.types.saml_idp.deserialize_json(data["Idp"])
    if "MasterUserName" in data:
        out["master_user_name"] = data["MasterUserName"]
    if "MasterBackendRole" in data:
        out["master_backend_role"] = data["MasterBackendRole"]
    if "SubjectKey" in data:
        out["subject_key"] = data["SubjectKey"]
    if "RolesKey" in data:
        out["roles_key"] = data["RolesKey"]
    if "SessionTimeoutMinutes" in data:
        out["session_timeout_minutes"] = data["SessionTimeoutMinutes"]
    return out
