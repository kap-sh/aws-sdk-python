"""Generated from Smithy shape ``com.amazonaws.vpclattice#ResourceConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_vpc_lattice.errors import DeserializationError

ResourceConfigurationType: TypeAlias = Literal[
    "GROUP",
    "CHILD",
    "SINGLE",
    "ARN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GROUP",
        "CHILD",
        "SINGLE",
        "ARN",
    )
)


def serialize_json(value: ResourceConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> ResourceConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceConfigurationType value: {data!r}")
    return cast(ResourceConfigurationType, data)
