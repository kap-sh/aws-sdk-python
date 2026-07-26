"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.login_auth_config_req_obj


class UpdateBackendConfigResponse(TypedDict, closed=True):
    app_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The app ID.</p>"""
    backend_manager_app_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The app ID for the backend manager.</p>"""
    error: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>If the request fails, this error is returned.</p>"""
    login_auth_config: NotRequired[
        "capo_amplifybackend.types.login_auth_config_req_obj.LoginAuthConfigReqObj"
    ]
    """<p>Describes the Amazon Cognito configurations for the Admin UI auth resource to log in with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendConfigResponse) -> dict:
    out: dict = {}
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "backend_manager_app_id" in value:
        out["backendManagerAppId"] = value["backend_manager_app_id"]
    if "error" in value:
        out["error"] = value["error"]
    if "login_auth_config" in value:
        import capo_amplifybackend.types.login_auth_config_req_obj

        out["loginAuthConfig"] = (
            capo_amplifybackend.types.login_auth_config_req_obj.serialize_json(
                value["login_auth_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBackendConfigResponse:
    out: UpdateBackendConfigResponse = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    if "backendManagerAppId" in data:
        out["backend_manager_app_id"] = data["backendManagerAppId"]
    if "error" in data:
        out["error"] = data["error"]
    if "loginAuthConfig" in data:
        import capo_amplifybackend.types.login_auth_config_req_obj

        out["login_auth_config"] = (
            capo_amplifybackend.types.login_auth_config_req_obj.deserialize_json(
                data["loginAuthConfig"]
            )
        )
    return out
