"""Generated from Smithy shape ``com.amazonaws.deadline#CustomerManagedFleetOperatingSystemFamily``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

CustomerManagedFleetOperatingSystemFamily: TypeAlias = Literal[
    "WINDOWS",
    "LINUX",
    "MACOS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WINDOWS",
        "LINUX",
        "MACOS",
    )
)


def serialize_json(value: CustomerManagedFleetOperatingSystemFamily) -> str:
    return value


def deserialize_json(data: str) -> CustomerManagedFleetOperatingSystemFamily:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomerManagedFleetOperatingSystemFamily value: {data!r}"
        )
    return cast(CustomerManagedFleetOperatingSystemFamily, data)
