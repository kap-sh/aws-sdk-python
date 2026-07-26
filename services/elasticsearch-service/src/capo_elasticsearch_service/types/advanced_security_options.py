"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AdvancedSecurityOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.disable_timestamp
    import capo_elasticsearch_service.types.saml_options_output


class AdvancedSecurityOptions(TypedDict, closed=True):
    enabled: NotRequired["capo_elasticsearch_service.types.boolean.Boolean"]
    """<p>True if advanced security is enabled.</p>"""
    internal_user_database_enabled: NotRequired[
        "capo_elasticsearch_service.types.boolean.Boolean"
    ]
    """<p>True if the internal user database is enabled.</p>"""
    saml_options: NotRequired[
        "capo_elasticsearch_service.types.saml_options_output.SAMLOptionsOutput"
    ]
    """<p>Describes the SAML application configured for a domain.</p>"""
    anonymous_auth_disable_date: NotRequired[
        "capo_elasticsearch_service.types.disable_timestamp.DisableTimestamp"
    ]
    """<p>Specifies the Anonymous Auth Disable Date when Anonymous Auth is enabled.</p>"""
    anonymous_auth_enabled: NotRequired[
        "capo_elasticsearch_service.types.boolean.Boolean"
    ]
    """<p>True if Anonymous auth is enabled. Anonymous auth can be enabled only when AdvancedSecurity is enabled on existing domains.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedSecurityOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "internal_user_database_enabled" in value:
        out["InternalUserDatabaseEnabled"] = value["internal_user_database_enabled"]
    if "saml_options" in value:
        import capo_elasticsearch_service.types.saml_options_output

        out["SAMLOptions"] = (
            capo_elasticsearch_service.types.saml_options_output.serialize_json(
                value["saml_options"]
            )
        )
    if "anonymous_auth_disable_date" in value:
        import capo_elasticsearch_service.types.disable_timestamp

        out["AnonymousAuthDisableDate"] = (
            capo_elasticsearch_service.types.disable_timestamp.serialize_json(
                value["anonymous_auth_disable_date"]
            )
        )
    if "anonymous_auth_enabled" in value:
        out["AnonymousAuthEnabled"] = value["anonymous_auth_enabled"]
    return out


def deserialize_json(data: dict) -> AdvancedSecurityOptions:
    out: AdvancedSecurityOptions = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "InternalUserDatabaseEnabled" in data:
        out["internal_user_database_enabled"] = data["InternalUserDatabaseEnabled"]
    if "SAMLOptions" in data:
        import capo_elasticsearch_service.types.saml_options_output

        out["saml_options"] = (
            capo_elasticsearch_service.types.saml_options_output.deserialize_json(
                data["SAMLOptions"]
            )
        )
    if "AnonymousAuthDisableDate" in data:
        import capo_elasticsearch_service.types.disable_timestamp

        out["anonymous_auth_disable_date"] = (
            capo_elasticsearch_service.types.disable_timestamp.deserialize_json(
                data["AnonymousAuthDisableDate"]
            )
        )
    if "AnonymousAuthEnabled" in data:
        out["anonymous_auth_enabled"] = data["AnonymousAuthEnabled"]
    return out
