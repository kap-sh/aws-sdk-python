"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeviceListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.device_type

DeviceListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.device_type.DeviceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceListType) -> list:
    import aws_sdk_cognito_identity_provider.types.device_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.device_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeviceListType:
    import aws_sdk_cognito_identity_provider.types.device_type

    out: DeviceListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.device_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
