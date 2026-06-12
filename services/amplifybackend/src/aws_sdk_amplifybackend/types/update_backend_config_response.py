"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string
    import aws_sdk_amplifybackend.types.login_auth_config_req_obj


class UpdateBackendConfigResponse(TypedDict):
    app_id: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The app ID.</p>"""
    backend_manager_app_id: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>The app ID for the backend manager.</p>"""
    error: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>If the request fails, this error is returned.</p>"""
    login_auth_config: NotRequired[
        "aws_sdk_amplifybackend.types.login_auth_config_req_obj.LoginAuthConfigReqObj"
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
        import aws_sdk_amplifybackend.types.login_auth_config_req_obj

        out["loginAuthConfig"] = (
            aws_sdk_amplifybackend.types.login_auth_config_req_obj.serialize_json(
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
        import aws_sdk_amplifybackend.types.login_auth_config_req_obj

        out["login_auth_config"] = (
            aws_sdk_amplifybackend.types.login_auth_config_req_obj.deserialize_json(
                data["loginAuthConfig"]
            )
        )
    return out
