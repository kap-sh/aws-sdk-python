"""Generated from Smithy shape ``com.amazonaws.dlm#DefaultPoliciesTypeValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dlm.errors import DeserializationError

DefaultPoliciesTypeValues: TypeAlias = Literal[
    "VOLUME",
    "INSTANCE",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VOLUME",
        "INSTANCE",
        "ALL",
    )
)


def serialize_json(value: DefaultPoliciesTypeValues) -> str:
    return value


def deserialize_json(data: str) -> DefaultPoliciesTypeValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DefaultPoliciesTypeValues value: {data!r}")
    return cast(DefaultPoliciesTypeValues, data)
