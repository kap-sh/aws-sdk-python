"""Generated from Smithy shape ``com.amazonaws.dlm#DefaultPolicyTypeValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

DefaultPolicyTypeValues: TypeAlias = Literal[
    "VOLUME",
    "INSTANCE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VOLUME",
        "INSTANCE",
    )
)


def serialize_json(value: DefaultPolicyTypeValues) -> str:
    return value


def deserialize_json(data: str) -> DefaultPolicyTypeValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DefaultPolicyTypeValues value: {data!r}")
    return cast(DefaultPolicyTypeValues, data)
