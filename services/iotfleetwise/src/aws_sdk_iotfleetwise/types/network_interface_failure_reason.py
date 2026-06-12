"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NetworkInterfaceFailureReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

NetworkInterfaceFailureReason: TypeAlias = Literal[
    "DUPLICATE_NETWORK_INTERFACE",
    "CONFLICTING_NETWORK_INTERFACE",
    "NETWORK_INTERFACE_TO_ADD_ALREADY_EXISTS",
    "CAN_NETWORK_INTERFACE_INFO_IS_NULL",
    "OBD_NETWORK_INTERFACE_INFO_IS_NULL",
    "NETWORK_INTERFACE_TO_REMOVE_ASSOCIATED_WITH_SIGNALS",
    "VEHICLE_MIDDLEWARE_NETWORK_INTERFACE_INFO_IS_NULL",
    "CUSTOM_DECODING_SIGNAL_NETWORK_INTERFACE_INFO_IS_NULL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DUPLICATE_NETWORK_INTERFACE",
        "CONFLICTING_NETWORK_INTERFACE",
        "NETWORK_INTERFACE_TO_ADD_ALREADY_EXISTS",
        "CAN_NETWORK_INTERFACE_INFO_IS_NULL",
        "OBD_NETWORK_INTERFACE_INFO_IS_NULL",
        "NETWORK_INTERFACE_TO_REMOVE_ASSOCIATED_WITH_SIGNALS",
        "VEHICLE_MIDDLEWARE_NETWORK_INTERFACE_INFO_IS_NULL",
        "CUSTOM_DECODING_SIGNAL_NETWORK_INTERFACE_INFO_IS_NULL",
    )
)


def serialize_aws_json_1_0(value: NetworkInterfaceFailureReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NetworkInterfaceFailureReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NetworkInterfaceFailureReason value: {data!r}"
        )
    return cast(NetworkInterfaceFailureReason, data)
