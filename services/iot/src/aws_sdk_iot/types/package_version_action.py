"""Generated from Smithy shape ``com.amazonaws.iot#PackageVersionAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

PackageVersionAction: TypeAlias = Literal[
    "PUBLISH",
    "DEPRECATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISH",
        "DEPRECATE",
    )
)


def serialize_json(value: PackageVersionAction) -> str:
    return value


def deserialize_json(data: str) -> PackageVersionAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageVersionAction value: {data!r}")
    return cast(PackageVersionAction, data)
