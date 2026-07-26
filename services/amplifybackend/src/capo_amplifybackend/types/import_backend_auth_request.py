"""Generated from Smithy shape ``com.amazonaws.amplifybackend#ImportBackendAuthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string


class ImportBackendAuthRequest(TypedDict, closed=True):
    app_id: "capo_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "capo_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""
    identity_pool_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The ID of the Amazon Cognito identity pool.</p>"""
    native_client_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The ID of the Amazon Cognito native client.</p>"""
    user_pool_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The ID of the Amazon Cognito user pool.</p>"""
    web_client_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The ID of the Amazon Cognito web client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportBackendAuthRequest) -> dict:
    out: dict = {}
    if "identity_pool_id" in value:
        out["identityPoolId"] = value["identity_pool_id"]
    if "native_client_id" in value:
        out["nativeClientId"] = value["native_client_id"]
    if "user_pool_id" in value:
        out["userPoolId"] = value["user_pool_id"]
    if "web_client_id" in value:
        out["webClientId"] = value["web_client_id"]
    return out


def deserialize_json(data: dict) -> ImportBackendAuthRequest:
    out: ImportBackendAuthRequest = {}  # type: ignore[typeddict-item]
    if "identityPoolId" in data:
        out["identity_pool_id"] = data["identityPoolId"]
    if "nativeClientId" in data:
        out["native_client_id"] = data["nativeClientId"]
    if "userPoolId" in data:
        out["user_pool_id"] = data["userPoolId"]
    if "webClientId" in data:
        out["web_client_id"] = data["webClientId"]
    return out
