"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NetworkInterfaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

NetworkInterfaceType: TypeAlias = Literal[
    "CAN_INTERFACE",
    "OBD_INTERFACE",
    "VEHICLE_MIDDLEWARE",
    "CUSTOM_DECODING_INTERFACE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CAN_INTERFACE",
        "OBD_INTERFACE",
        "VEHICLE_MIDDLEWARE",
        "CUSTOM_DECODING_INTERFACE",
    )
)


def serialize_aws_json_1_0(value: NetworkInterfaceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NetworkInterfaceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkInterfaceType value: {data!r}")
    return cast(NetworkInterfaceType, data)
