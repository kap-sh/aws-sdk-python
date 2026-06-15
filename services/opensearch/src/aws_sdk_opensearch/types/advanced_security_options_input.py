"""Generated from Smithy shape ``com.amazonaws.opensearch#AdvancedSecurityOptionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.iam_federation_options_input
    import aws_sdk_opensearch.types.jwt_options_input
    import aws_sdk_opensearch.types.master_user_options
    import aws_sdk_opensearch.types.saml_options_input


class AdvancedSecurityOptionsInput(TypedDict):
    enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>True to enable fine-grained access control.</p>"""
    internal_user_database_enabled: NotRequired[
        "aws_sdk_opensearch.types.boolean.Boolean"
    ]
    """<p>True to enable the internal user database.</p>"""
    master_user_options: NotRequired[
        "aws_sdk_opensearch.types.master_user_options.MasterUserOptions"
    ]
    """<p>Container for information about the master user.</p>"""
    saml_options: NotRequired[
        "aws_sdk_opensearch.types.saml_options_input.SAMLOptionsInput"
    ]
    """<p>Container for information about the SAML configuration for OpenSearch Dashboards.</p>"""
    jwt_options: NotRequired[
        "aws_sdk_opensearch.types.jwt_options_input.JWTOptionsInput"
    ]
    """<p>Container for information about the JWT configuration of the Amazon OpenSearch Service. </p>"""
    iam_federation_options: NotRequired[
        "aws_sdk_opensearch.types.iam_federation_options_input.IAMFederationOptionsInput"
    ]
    """<p>Input configuration for IAM identity federation within advanced security options.</p>"""
    anonymous_auth_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    r"""<p>True to enable a 30-day migration period during which administrators can create role mappings. Only necessary when <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html#fgac-enabling-existing\">enabling fine-grained access control on an existing domain</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedSecurityOptionsInput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "internal_user_database_enabled" in value:
        out["InternalUserDatabaseEnabled"] = value["internal_user_database_enabled"]
    if "master_user_options" in value:
        import aws_sdk_opensearch.types.master_user_options

        out["MasterUserOptions"] = (
            aws_sdk_opensearch.types.master_user_options.serialize_json(
                value["master_user_options"]
            )
        )
    if "saml_options" in value:
        import aws_sdk_opensearch.types.saml_options_input

        out["SAMLOptions"] = aws_sdk_opensearch.types.saml_options_input.serialize_json(
            value["saml_options"]
        )
    if "jwt_options" in value:
        import aws_sdk_opensearch.types.jwt_options_input

        out["JWTOptions"] = aws_sdk_opensearch.types.jwt_options_input.serialize_json(
            value["jwt_options"]
        )
    if "iam_federation_options" in value:
        import aws_sdk_opensearch.types.iam_federation_options_input

        out["IAMFederationOptions"] = (
            aws_sdk_opensearch.types.iam_federation_options_input.serialize_json(
                value["iam_federation_options"]
            )
        )
    if "anonymous_auth_enabled" in value:
        out["AnonymousAuthEnabled"] = value["anonymous_auth_enabled"]
    return out


def deserialize_json(data: dict) -> AdvancedSecurityOptionsInput:
    out: AdvancedSecurityOptionsInput = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "InternalUserDatabaseEnabled" in data:
        out["internal_user_database_enabled"] = data["InternalUserDatabaseEnabled"]
    if "MasterUserOptions" in data:
        import aws_sdk_opensearch.types.master_user_options

        out["master_user_options"] = (
            aws_sdk_opensearch.types.master_user_options.deserialize_json(
                data["MasterUserOptions"]
            )
        )
    if "SAMLOptions" in data:
        import aws_sdk_opensearch.types.saml_options_input

        out["saml_options"] = (
            aws_sdk_opensearch.types.saml_options_input.deserialize_json(
                data["SAMLOptions"]
            )
        )
    if "JWTOptions" in data:
        import aws_sdk_opensearch.types.jwt_options_input

        out["jwt_options"] = (
            aws_sdk_opensearch.types.jwt_options_input.deserialize_json(
                data["JWTOptions"]
            )
        )
    if "IAMFederationOptions" in data:
        import aws_sdk_opensearch.types.iam_federation_options_input

        out["iam_federation_options"] = (
            aws_sdk_opensearch.types.iam_federation_options_input.deserialize_json(
                data["IAMFederationOptions"]
            )
        )
    if "AnonymousAuthEnabled" in data:
        out["anonymous_auth_enabled"] = data["AnonymousAuthEnabled"]
    return out
