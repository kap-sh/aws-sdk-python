"""Generated from Smithy shape ``com.amazonaws.snowball#TargetOnDeviceServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.target_on_device_service

TargetOnDeviceServiceList: TypeAlias = list[
    "capo_snowball.types.target_on_device_service.TargetOnDeviceService"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetOnDeviceServiceList) -> list:
    import capo_snowball.types.target_on_device_service

    out: list = []
    for item in value:
        out.append(
            capo_snowball.types.target_on_device_service.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TargetOnDeviceServiceList:
    import capo_snowball.types.target_on_device_service

    out: TargetOnDeviceServiceList = []
    for item in data:
        out.append(
            capo_snowball.types.target_on_device_service.deserialize_aws_json_1_1(item)
        )
    return out
