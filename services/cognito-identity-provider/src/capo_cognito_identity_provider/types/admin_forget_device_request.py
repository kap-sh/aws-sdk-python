"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminForgetDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.device_key_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.username_type


class AdminForgetDeviceRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where the device owner is a user.</p>"""
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If <code>username</code> isn't an alias attribute in your user pool, this value must be the <code>sub</code> of a local user or the username of a user from a third-party IdP.</p>"""
    device_key: "capo_cognito_identity_provider.types.device_key_type.DeviceKeyType"
    """<p>The key ID of the device that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminForgetDeviceRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    out["DeviceKey"] = value["device_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminForgetDeviceRequest:
    out: AdminForgetDeviceRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("AdminForgetDeviceRequest.user_pool_id required")
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("AdminForgetDeviceRequest.username required")
    if "DeviceKey" in data:
        out["device_key"] = data["DeviceKey"]
    else:
        raise DeserializationError("AdminForgetDeviceRequest.device_key required")
    return out
