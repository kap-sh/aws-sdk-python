"""Generated from Smithy shape ``com.amazonaws.grafana#AuthenticationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.authentication_providers
    import aws_sdk_grafana.types.saml_configuration_status


class AuthenticationSummary(TypedDict):
    providers: "aws_sdk_grafana.types.authentication_providers.AuthenticationProviders"
    """<p>Specifies whether the workspace uses SAML, IAM Identity Center, or both methods for user authentication.</p>"""
    saml_configuration_status: NotRequired[
        "aws_sdk_grafana.types.saml_configuration_status.SamlConfigurationStatus"
    ]
    """<p>Specifies whether the workplace's user authentication method is fully configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationSummary) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.authentication_providers

    out["providers"] = aws_sdk_grafana.types.authentication_providers.serialize_json(
        value["providers"]
    )
    if "saml_configuration_status" in value:
        out["samlConfigurationStatus"] = value["saml_configuration_status"]
    return out


def deserialize_json(data: dict) -> AuthenticationSummary:
    out: AuthenticationSummary = {}  # type: ignore[typeddict-item]
    if "providers" in data:
        import aws_sdk_grafana.types.authentication_providers

        out["providers"] = (
            aws_sdk_grafana.types.authentication_providers.deserialize_json(
                data["providers"]
            )
        )
    else:
        raise DeserializationError("AuthenticationSummary.providers required")
    if "samlConfigurationStatus" in data:
        out["saml_configuration_status"] = data["samlConfigurationStatus"]
    return out
