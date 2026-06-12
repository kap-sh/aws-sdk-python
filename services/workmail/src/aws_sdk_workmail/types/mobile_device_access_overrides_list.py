"""Generated from Smithy shape ``com.amazonaws.workmail#MobileDeviceAccessOverridesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.mobile_device_access_override

MobileDeviceAccessOverridesList: TypeAlias = list[
    "aws_sdk_workmail.types.mobile_device_access_override.MobileDeviceAccessOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MobileDeviceAccessOverridesList) -> list:
    import aws_sdk_workmail.types.mobile_device_access_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workmail.types.mobile_device_access_override.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MobileDeviceAccessOverridesList:
    import aws_sdk_workmail.types.mobile_device_access_override

    out: MobileDeviceAccessOverridesList = []
    for item in data:
        out.append(
            aws_sdk_workmail.types.mobile_device_access_override.deserialize_aws_json_1_1(
                item
            )
        )
    return out
