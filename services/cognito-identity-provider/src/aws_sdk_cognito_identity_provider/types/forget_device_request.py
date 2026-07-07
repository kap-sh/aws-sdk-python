"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ForgetDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.device_key_type
    import aws_sdk_cognito_identity_provider.types.token_model_type


class ForgetDeviceRequest(TypedDict, closed=True):
    access_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    device_key: "aws_sdk_cognito_identity_provider.types.device_key_type.DeviceKeyType"
    """<p>The unique identifier, or device key, of the device that the user wants to forget.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForgetDeviceRequest) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["AccessToken"] = value["access_token"]
    out["DeviceKey"] = value["device_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ForgetDeviceRequest:
    out: ForgetDeviceRequest = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    if "DeviceKey" in data:
        out["device_key"] = data["DeviceKey"]
    else:
        raise DeserializationError("ForgetDeviceRequest.device_key required")
    return out
