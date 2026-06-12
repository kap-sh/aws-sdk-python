"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AuthConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.auth_materials
    import aws_sdk_iot_managed_integrations.types.o_auth_config


class AuthConfig(TypedDict):
    o_auth: NotRequired[
        "aws_sdk_iot_managed_integrations.types.o_auth_config.OAuthConfig"
    ]
    """<p>The OAuth configuration settings used for authentication with the third-party service.</p>"""
    general_authorization: NotRequired[
        "aws_sdk_iot_managed_integrations.types.auth_materials.AuthMaterials"
    ]
    """<p>The authorization materials for General Authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthConfig) -> dict:
    out: dict = {}
    if "o_auth" in value:
        import aws_sdk_iot_managed_integrations.types.o_auth_config

        out["oAuth"] = (
            aws_sdk_iot_managed_integrations.types.o_auth_config.serialize_json(
                value["o_auth"]
            )
        )
    if "general_authorization" in value:
        import aws_sdk_iot_managed_integrations.types.auth_materials

        out["GeneralAuthorization"] = (
            aws_sdk_iot_managed_integrations.types.auth_materials.serialize_json(
                value["general_authorization"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthConfig:
    out: AuthConfig = {}  # type: ignore[typeddict-item]
    if "oAuth" in data:
        import aws_sdk_iot_managed_integrations.types.o_auth_config

        out["o_auth"] = (
            aws_sdk_iot_managed_integrations.types.o_auth_config.deserialize_json(
                data["oAuth"]
            )
        )
    if "GeneralAuthorization" in data:
        import aws_sdk_iot_managed_integrations.types.auth_materials

        out["general_authorization"] = (
            aws_sdk_iot_managed_integrations.types.auth_materials.deserialize_json(
                data["GeneralAuthorization"]
            )
        )
    return out
