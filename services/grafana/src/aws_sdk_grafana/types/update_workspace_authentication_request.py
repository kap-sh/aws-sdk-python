"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateWorkspaceAuthenticationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.authentication_providers
    import aws_sdk_grafana.types.saml_configuration
    import aws_sdk_grafana.types.workspace_id


class UpdateWorkspaceAuthenticationRequest(TypedDict):
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to update the authentication for.</p>"""
    authentication_providers: (
        "aws_sdk_grafana.types.authentication_providers.AuthenticationProviders"
    )
    r"""<p>Specifies whether this workspace uses SAML 2.0, IAM Identity Center, or both to authenticate users for using the Grafana console within a workspace. For more information, see <a href=\"https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html\">User authentication in Amazon Managed Grafana</a>.</p>"""
    saml_configuration: NotRequired[
        "aws_sdk_grafana.types.saml_configuration.SamlConfiguration"
    ]
    """<p>If the workspace uses SAML, use this structure to map SAML assertion attributes to workspace user information and define which groups in the assertion attribute are to have the <code>Admin</code> and <code>Editor</code> roles in the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceAuthenticationRequest) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.authentication_providers

    out["authenticationProviders"] = (
        aws_sdk_grafana.types.authentication_providers.serialize_json(
            value["authentication_providers"]
        )
    )
    if "saml_configuration" in value:
        import aws_sdk_grafana.types.saml_configuration

        out["samlConfiguration"] = (
            aws_sdk_grafana.types.saml_configuration.serialize_json(
                value["saml_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceAuthenticationRequest:
    out: UpdateWorkspaceAuthenticationRequest = {}  # type: ignore[typeddict-item]
    if "authenticationProviders" in data:
        import aws_sdk_grafana.types.authentication_providers

        out["authentication_providers"] = (
            aws_sdk_grafana.types.authentication_providers.deserialize_json(
                data["authenticationProviders"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateWorkspaceAuthenticationRequest.authentication_providers required"
        )
    if "samlConfiguration" in data:
        import aws_sdk_grafana.types.saml_configuration

        out["saml_configuration"] = (
            aws_sdk_grafana.types.saml_configuration.deserialize_json(
                data["samlConfiguration"]
            )
        )
    return out
