"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageScopeOperationEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

PackageScopeOperationEnum: TypeAlias = Literal[
    "ADD",
    "OVERRIDE",
    "REMOVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADD",
        "OVERRIDE",
        "REMOVE",
    )
)


def serialize_json(value: PackageScopeOperationEnum) -> str:
    return value


def deserialize_json(data: str) -> PackageScopeOperationEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageScopeOperationEnum value: {data!r}")
    return cast(PackageScopeOperationEnum, data)
