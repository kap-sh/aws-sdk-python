"""Generated from Smithy shape ``com.amazonaws.opensearch#AdvancedSecurityOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.disable_timestamp
    import aws_sdk_opensearch.types.iam_federation_options_output
    import aws_sdk_opensearch.types.jwt_options_output
    import aws_sdk_opensearch.types.saml_options_output


class AdvancedSecurityOptions(TypedDict):
    enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>True if fine-grained access control is enabled.</p>"""
    internal_user_database_enabled: NotRequired[
        "aws_sdk_opensearch.types.boolean.Boolean"
    ]
    """<p>True if the internal user database is enabled.</p>"""
    saml_options: NotRequired[
        "aws_sdk_opensearch.types.saml_options_output.SAMLOptionsOutput"
    ]
    """<p>Container for information about the SAML configuration for OpenSearch Dashboards.</p>"""
    jwt_options: NotRequired[
        "aws_sdk_opensearch.types.jwt_options_output.JWTOptionsOutput"
    ]
    """<p>Container for information about the JWT configuration of the Amazon OpenSearch Service.</p>"""
    iam_federation_options: NotRequired[
        "aws_sdk_opensearch.types.iam_federation_options_output.IAMFederationOptionsOutput"
    ]
    """<p>Configuration options for IAM identity federation in advanced security settings.</p>"""
    anonymous_auth_disable_date: NotRequired[
        "aws_sdk_opensearch.types.disable_timestamp.DisableTimestamp"
    ]
    """<p>Date and time when the migration period will be disabled. Only necessary when <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing\">enabling fine-grained access control on an existing domain</a>.</p>"""
    anonymous_auth_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>True if a 30-day migration period is enabled, during which administrators can create role mappings. Only necessary when <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing\">enabling fine-grained access control on an existing domain</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedSecurityOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "internal_user_database_enabled" in value:
        out["InternalUserDatabaseEnabled"] = value["internal_user_database_enabled"]
    if "saml_options" in value:
        import aws_sdk_opensearch.types.saml_options_output

        out["SAMLOptions"] = (
            aws_sdk_opensearch.types.saml_options_output.serialize_json(
                value["saml_options"]
            )
        )
    if "jwt_options" in value:
        import aws_sdk_opensearch.types.jwt_options_output

        out["JWTOptions"] = aws_sdk_opensearch.types.jwt_options_output.serialize_json(
            value["jwt_options"]
        )
    if "iam_federation_options" in value:
        import aws_sdk_opensearch.types.iam_federation_options_output

        out["IAMFederationOptions"] = (
            aws_sdk_opensearch.types.iam_federation_options_output.serialize_json(
                value["iam_federation_options"]
            )
        )
    if "anonymous_auth_disable_date" in value:
        import aws_sdk_opensearch.types.disable_timestamp

        out["AnonymousAuthDisableDate"] = (
            aws_sdk_opensearch.types.disable_timestamp.serialize_json(
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
        import aws_sdk_opensearch.types.saml_options_output

        out["saml_options"] = (
            aws_sdk_opensearch.types.saml_options_output.deserialize_json(
                data["SAMLOptions"]
            )
        )
    if "JWTOptions" in data:
        import aws_sdk_opensearch.types.jwt_options_output

        out["jwt_options"] = (
            aws_sdk_opensearch.types.jwt_options_output.deserialize_json(
                data["JWTOptions"]
            )
        )
    if "IAMFederationOptions" in data:
        import aws_sdk_opensearch.types.iam_federation_options_output

        out["iam_federation_options"] = (
            aws_sdk_opensearch.types.iam_federation_options_output.deserialize_json(
                data["IAMFederationOptions"]
            )
        )
    if "AnonymousAuthDisableDate" in data:
        import aws_sdk_opensearch.types.disable_timestamp

        out["anonymous_auth_disable_date"] = (
            aws_sdk_opensearch.types.disable_timestamp.deserialize_json(
                data["AnonymousAuthDisableDate"]
            )
        )
    if "AnonymousAuthEnabled" in data:
        out["anonymous_auth_enabled"] = data["AnonymousAuthEnabled"]
    return out
