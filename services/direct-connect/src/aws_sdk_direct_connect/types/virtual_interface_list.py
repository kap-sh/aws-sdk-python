"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.virtual_interface

VirtualInterfaceList: TypeAlias = list[
    "aws_sdk_direct_connect.types.virtual_interface.VirtualInterface"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualInterfaceList) -> list:
    import aws_sdk_direct_connect.types.virtual_interface

    out: list = []
    for item in value:
        out.append(
            aws_sdk_direct_connect.types.virtual_interface.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VirtualInterfaceList:
    import aws_sdk_direct_connect.types.virtual_interface

    out: VirtualInterfaceList = []
    for item in data:
        out.append(
            aws_sdk_direct_connect.types.virtual_interface.deserialize_aws_json_1_1(
                item
            )
        )
    return out
