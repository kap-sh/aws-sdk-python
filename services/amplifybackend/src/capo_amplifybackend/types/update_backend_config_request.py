"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.login_auth_config_req_obj


class UpdateBackendConfigRequest(TypedDict, closed=True):
    app_id: "capo_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    login_auth_config: NotRequired[
        "capo_amplifybackend.types.login_auth_config_req_obj.LoginAuthConfigReqObj"
    ]
    """<p>Describes the Amazon Cognito configuration for Admin UI access.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendConfigRequest) -> dict:
    out: dict = {}
    if "login_auth_config" in value:
        import capo_amplifybackend.types.login_auth_config_req_obj

        out["loginAuthConfig"] = (
            capo_amplifybackend.types.login_auth_config_req_obj.serialize_json(
                value["login_auth_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBackendConfigRequest:
    out: UpdateBackendConfigRequest = {}  # type: ignore[typeddict-item]
    if "loginAuthConfig" in data:
        import capo_amplifybackend.types.login_auth_config_req_obj

        out["login_auth_config"] = (
            capo_amplifybackend.types.login_auth_config_req_obj.deserialize_json(
                data["loginAuthConfig"]
            )
        )
    return out
