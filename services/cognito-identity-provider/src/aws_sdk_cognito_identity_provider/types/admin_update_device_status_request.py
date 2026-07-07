"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminUpdateDeviceStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.device_key_type
    import aws_sdk_cognito_identity_provider.types.device_remembered_status_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type
    import aws_sdk_cognito_identity_provider.types.username_type


class AdminUpdateDeviceStatusRequest(TypedDict, closed=True):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to change a user's device status.</p>"""
    username: "aws_sdk_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If <code>username</code> isn't an alias attribute in your user pool, this value must be the <code>sub</code> of a local user or the username of a user from a third-party IdP.</p>"""
    device_key: "aws_sdk_cognito_identity_provider.types.device_key_type.DeviceKeyType"
    """<p>The unique identifier, or device key, of the device that you want to update the status for.</p>"""
    device_remembered_status: NotRequired[
        "aws_sdk_cognito_identity_provider.types.device_remembered_status_type.DeviceRememberedStatusType"
    ]
    """<p>To enable device authentication with the specified device, set to <code>remembered</code>.To disable, set to <code>not_remembered</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminUpdateDeviceStatusRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    out["DeviceKey"] = value["device_key"]
    if "device_remembered_status" in value:
        import aws_sdk_cognito_identity_provider.types.device_remembered_status_type

        out["DeviceRememberedStatus"] = (
            aws_sdk_cognito_identity_provider.types.device_remembered_status_type.serialize_aws_json_1_1(
                value["device_remembered_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminUpdateDeviceStatusRequest:
    out: AdminUpdateDeviceStatusRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "AdminUpdateDeviceStatusRequest.user_pool_id required"
        )
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("AdminUpdateDeviceStatusRequest.username required")
    if "DeviceKey" in data:
        out["device_key"] = data["DeviceKey"]
    else:
        raise DeserializationError("AdminUpdateDeviceStatusRequest.device_key required")
    if "DeviceRememberedStatus" in data:
        import aws_sdk_cognito_identity_provider.types.device_remembered_status_type

        out["device_remembered_status"] = (
            aws_sdk_cognito_identity_provider.types.device_remembered_status_type.deserialize_aws_json_1_1(
                data["DeviceRememberedStatus"]
            )
        )
    return out
