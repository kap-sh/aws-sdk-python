"""Generated from Smithy shape ``com.amazonaws.deadline#ServiceManagedFleetOperatingSystemFamily``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

ServiceManagedFleetOperatingSystemFamily: TypeAlias = Literal[
    "WINDOWS",
    "LINUX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WINDOWS",
        "LINUX",
    )
)


def serialize_json(value: ServiceManagedFleetOperatingSystemFamily) -> str:
    return value


def deserialize_json(data: str) -> ServiceManagedFleetOperatingSystemFamily:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceManagedFleetOperatingSystemFamily value: {data!r}"
        )
    return cast(ServiceManagedFleetOperatingSystemFamily, data)
