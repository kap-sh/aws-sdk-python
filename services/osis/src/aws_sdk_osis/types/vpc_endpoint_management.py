"""Generated from Smithy shape ``com.amazonaws.osis#VpcEndpointManagement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_osis.errors import DeserializationError

VpcEndpointManagement: TypeAlias = Literal[
    "CUSTOMER",
    "SERVICE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER",
        "SERVICE",
    )
)


def serialize_json(value: VpcEndpointManagement) -> str:
    return value


def deserialize_json(data: str) -> VpcEndpointManagement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VpcEndpointManagement value: {data!r}")
    return cast(VpcEndpointManagement, data)
