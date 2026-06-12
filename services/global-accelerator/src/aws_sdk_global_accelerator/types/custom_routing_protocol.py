"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_global_accelerator.errors import DeserializationError

CustomRoutingProtocol: TypeAlias = Literal[
    "TCP",
    "UDP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TCP",
        "UDP",
    )
)


def serialize_aws_json_1_1(value: CustomRoutingProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomRoutingProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomRoutingProtocol value: {data!r}")
    return cast(CustomRoutingProtocol, data)
