"""Generated from Smithy shape ``com.amazonaws.lambda#PackageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

PackageType: TypeAlias = Literal[
    "Zip",
    "Image",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Zip",
        "Image",
    )
)


def serialize_json(value: PackageType) -> str:
    return value


def deserialize_json(data: str) -> PackageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageType value: {data!r}")
    return cast(PackageType, data)
