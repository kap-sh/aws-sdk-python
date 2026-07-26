"""Generated from Smithy shape ``com.amazonaws.workspaces#ClientDeviceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.client_device_type

ClientDeviceTypeList: TypeAlias = list[
    "capo_workspaces.types.client_device_type.ClientDeviceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientDeviceTypeList) -> list:
    import capo_workspaces.types.client_device_type

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.client_device_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClientDeviceTypeList:
    import capo_workspaces.types.client_device_type

    out: ClientDeviceTypeList = []
    for item in data:
        out.append(
            capo_workspaces.types.client_device_type.deserialize_aws_json_1_1(item)
        )
    return out
