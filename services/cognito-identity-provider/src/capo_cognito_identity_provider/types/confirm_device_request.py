"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ConfirmDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.device_key_type
    import capo_cognito_identity_provider.types.device_name_type
    import capo_cognito_identity_provider.types.device_secret_verifier_config_type
    import capo_cognito_identity_provider.types.token_model_type


class ConfirmDeviceRequest(TypedDict, closed=True):
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    device_key: "capo_cognito_identity_provider.types.device_key_type.DeviceKeyType"
    """<p>The unique identifier, or device key, of the device that you want to update the status for.</p>"""
    device_secret_verifier_config: NotRequired[
        "capo_cognito_identity_provider.types.device_secret_verifier_config_type.DeviceSecretVerifierConfigType"
    ]
    """<p>The configuration of the device secret verifier.</p>"""
    device_name: NotRequired[
        "capo_cognito_identity_provider.types.device_name_type.DeviceNameType"
    ]
    """<p>A friendly name for the device, for example <code>MyMobilePhone</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfirmDeviceRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    out["DeviceKey"] = value["device_key"]
    if "device_secret_verifier_config" in value:
        import capo_cognito_identity_provider.types.device_secret_verifier_config_type

        out["DeviceSecretVerifierConfig"] = (
            capo_cognito_identity_provider.types.device_secret_verifier_config_type.serialize_aws_json_1_1(
                value["device_secret_verifier_config"]
            )
        )
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfirmDeviceRequest:
    out: ConfirmDeviceRequest = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError("ConfirmDeviceRequest.access_token required")
    if "DeviceKey" in data:
        out["device_key"] = data["DeviceKey"]
    else:
        raise DeserializationError("ConfirmDeviceRequest.device_key required")
    if "DeviceSecretVerifierConfig" in data:
        import capo_cognito_identity_provider.types.device_secret_verifier_config_type

        out["device_secret_verifier_config"] = (
            capo_cognito_identity_provider.types.device_secret_verifier_config_type.deserialize_aws_json_1_1(
                data["DeviceSecretVerifierConfig"]
            )
        )
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    return out
