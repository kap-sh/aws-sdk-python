"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#NewDeviceMetadataType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.device_key_type
    import aws_sdk_cognito_identity_provider.types.string_type


class NewDeviceMetadataType(TypedDict, closed=True):
    device_key: NotRequired[
        "aws_sdk_cognito_identity_provider.types.device_key_type.DeviceKeyType"
    ]
    """<p>The device key, an identifier used in generating the <code>DEVICE_PASSWORD_VERIFIER</code> for device SRP authentication.</p>"""
    device_group_key: NotRequired[
        "aws_sdk_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The device group key, an identifier used in generating the <code>DEVICE_PASSWORD_VERIFIER</code> for device SRP authentication.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NewDeviceMetadataType) -> dict:
    out: dict = {}
    if "device_key" in value:
        out["DeviceKey"] = value["device_key"]
    if "device_group_key" in value:
        out["DeviceGroupKey"] = value["device_group_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NewDeviceMetadataType:
    out: NewDeviceMetadataType = {}  # type: ignore[typeddict-item]
    if "DeviceKey" in data:
        out["device_key"] = data["DeviceKey"]
    if "DeviceGroupKey" in data:
        out["device_group_key"] = data["DeviceGroupKey"]
    return out
