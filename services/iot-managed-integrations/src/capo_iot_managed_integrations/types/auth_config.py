"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AuthConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.auth_materials
    import capo_iot_managed_integrations.types.o_auth_config


class AuthConfig(TypedDict, closed=True):
    o_auth: NotRequired["capo_iot_managed_integrations.types.o_auth_config.OAuthConfig"]
    """<p>The OAuth configuration settings used for authentication with the third-party service.</p>"""
    general_authorization: NotRequired[
        "capo_iot_managed_integrations.types.auth_materials.AuthMaterials"
    ]
    """<p>The authorization materials for General Authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthConfig) -> dict:
    out: dict = {}
    if "o_auth" in value:
        import capo_iot_managed_integrations.types.o_auth_config

        out["oAuth"] = capo_iot_managed_integrations.types.o_auth_config.serialize_json(
            value["o_auth"]
        )
    if "general_authorization" in value:
        import capo_iot_managed_integrations.types.auth_materials

        out["GeneralAuthorization"] = (
            capo_iot_managed_integrations.types.auth_materials.serialize_json(
                value["general_authorization"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthConfig:
    out: AuthConfig = {}  # type: ignore[typeddict-item]
    if "oAuth" in data:
        import capo_iot_managed_integrations.types.o_auth_config

        out["o_auth"] = (
            capo_iot_managed_integrations.types.o_auth_config.deserialize_json(
                data["oAuth"]
            )
        )
    if "GeneralAuthorization" in data:
        import capo_iot_managed_integrations.types.auth_materials

        out["general_authorization"] = (
            capo_iot_managed_integrations.types.auth_materials.deserialize_json(
                data["GeneralAuthorization"]
            )
        )
    return out
