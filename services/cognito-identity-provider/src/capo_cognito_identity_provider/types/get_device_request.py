"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.device_key_type
    import capo_cognito_identity_provider.types.token_model_type


class GetDeviceRequest(TypedDict, closed=True):
    device_key: "capo_cognito_identity_provider.types.device_key_type.DeviceKeyType"
    """<p>The key of the device that you want to get information about.</p>"""
    access_token: NotRequired[
        "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeviceRequest) -> dict:
    out: dict = {}
    out["DeviceKey"] = value["device_key"]
    if "access_token" in value:
        out["AccessToken"] = value["access_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeviceRequest:
    out: GetDeviceRequest = {}  # type: ignore[typeddict-item]
    if "DeviceKey" in data:
        out["device_key"] = data["DeviceKey"]
    else:
        raise DeserializationError("GetDeviceRequest.device_key required")
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    return out
