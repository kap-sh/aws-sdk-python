"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NetworkInterfaceType``."""

from typing import Literal, TypeAlias, cast

NetworkInterfaceType: TypeAlias = Literal[
    "CAN_INTERFACE",
    "OBD_INTERFACE",
    "VEHICLE_MIDDLEWARE",
    "CUSTOM_DECODING_INTERFACE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkInterfaceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NetworkInterfaceType:
    return cast(NetworkInterfaceType, data)
