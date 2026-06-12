"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AuthConfigUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.general_authorization_update
    import aws_sdk_iot_managed_integrations.types.o_auth_update


class AuthConfigUpdate(TypedDict):
    o_auth_update: NotRequired[
        "aws_sdk_iot_managed_integrations.types.o_auth_update.OAuthUpdate"
    ]
    """<p>The updated OAuth configuration settings for the authentication configuration.</p>"""
    general_authorization_update: NotRequired[
        "aws_sdk_iot_managed_integrations.types.general_authorization_update.GeneralAuthorizationUpdate"
    ]
    """<p>The General Authorization update information containing authorization materials to add or update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthConfigUpdate) -> dict:
    out: dict = {}
    if "o_auth_update" in value:
        import aws_sdk_iot_managed_integrations.types.o_auth_update

        out["oAuthUpdate"] = (
            aws_sdk_iot_managed_integrations.types.o_auth_update.serialize_json(
                value["o_auth_update"]
            )
        )
    if "general_authorization_update" in value:
        import aws_sdk_iot_managed_integrations.types.general_authorization_update

        out["GeneralAuthorizationUpdate"] = (
            aws_sdk_iot_managed_integrations.types.general_authorization_update.serialize_json(
                value["general_authorization_update"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthConfigUpdate:
    out: AuthConfigUpdate = {}  # type: ignore[typeddict-item]
    if "oAuthUpdate" in data:
        import aws_sdk_iot_managed_integrations.types.o_auth_update

        out["o_auth_update"] = (
            aws_sdk_iot_managed_integrations.types.o_auth_update.deserialize_json(
                data["oAuthUpdate"]
            )
        )
    if "GeneralAuthorizationUpdate" in data:
        import aws_sdk_iot_managed_integrations.types.general_authorization_update

        out["general_authorization_update"] = (
            aws_sdk_iot_managed_integrations.types.general_authorization_update.deserialize_json(
                data["GeneralAuthorizationUpdate"]
            )
        )
    return out
