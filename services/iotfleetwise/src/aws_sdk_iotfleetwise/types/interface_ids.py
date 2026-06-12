"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#InterfaceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.interface_id

InterfaceIds: TypeAlias = list["aws_sdk_iotfleetwise.types.interface_id.InterfaceId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InterfaceIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> InterfaceIds:
    return list(data)
