"""Generated from Smithy shape ``com.amazonaws.ssmsap#AllocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

AllocationType: TypeAlias = Literal[
    "VPC_SUBNET",
    "ELASTIC_IP",
    "OVERLAY",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VPC_SUBNET",
        "ELASTIC_IP",
        "OVERLAY",
        "UNKNOWN",
    )
)


def serialize_json(value: AllocationType) -> str:
    return value


def deserialize_json(data: str) -> AllocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AllocationType value: {data!r}")
    return cast(AllocationType, data)
