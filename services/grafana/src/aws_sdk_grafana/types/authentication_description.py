"""Generated from Smithy shape ``com.amazonaws.grafana#AuthenticationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.authentication_providers
    import aws_sdk_grafana.types.aws_sso_authentication
    import aws_sdk_grafana.types.saml_authentication


class AuthenticationDescription(TypedDict):
    providers: "aws_sdk_grafana.types.authentication_providers.AuthenticationProviders"
    """<p>Specifies whether this workspace uses IAM Identity Center, SAML, or both methods to authenticate users to use the Grafana console in the Amazon Managed Grafana workspace.</p>"""
    saml: NotRequired["aws_sdk_grafana.types.saml_authentication.SamlAuthentication"]
    """<p>A structure containing information about how this workspace works with SAML, including what attributes within the assertion are to be mapped to user information in the workspace. </p>"""
    aws_sso: NotRequired[
        "aws_sdk_grafana.types.aws_sso_authentication.AwsSsoAuthentication"
    ]
    """<p>A structure containing information about how this workspace works with IAM Identity Center. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationDescription) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.authentication_providers

    out["providers"] = aws_sdk_grafana.types.authentication_providers.serialize_json(
        value["providers"]
    )
    if "saml" in value:
        import aws_sdk_grafana.types.saml_authentication

        out["saml"] = aws_sdk_grafana.types.saml_authentication.serialize_json(
            value["saml"]
        )
    if "aws_sso" in value:
        import aws_sdk_grafana.types.aws_sso_authentication

        out["awsSso"] = aws_sdk_grafana.types.aws_sso_authentication.serialize_json(
            value["aws_sso"]
        )
    return out


def deserialize_json(data: dict) -> AuthenticationDescription:
    out: AuthenticationDescription = {}  # type: ignore[typeddict-item]
    if "providers" in data:
        import aws_sdk_grafana.types.authentication_providers

        out["providers"] = (
            aws_sdk_grafana.types.authentication_providers.deserialize_json(
                data["providers"]
            )
        )
    else:
        raise DeserializationError("AuthenticationDescription.providers required")
    if "saml" in data:
        import aws_sdk_grafana.types.saml_authentication

        out["saml"] = aws_sdk_grafana.types.saml_authentication.deserialize_json(
            data["saml"]
        )
    if "awsSso" in data:
        import aws_sdk_grafana.types.aws_sso_authentication

        out["aws_sso"] = aws_sdk_grafana.types.aws_sso_authentication.deserialize_json(
            data["awsSso"]
        )
    return out
