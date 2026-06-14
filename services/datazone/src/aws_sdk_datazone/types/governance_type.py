"""Generated from Smithy shape ``com.amazonaws.datazone#GovernanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

GovernanceType: TypeAlias = Literal[
    "AWS_MANAGED",
    "USER_MANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_MANAGED",
        "USER_MANAGED",
    )
)


def serialize_json(value: GovernanceType) -> str:
    return value


def deserialize_json(data: str) -> GovernanceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GovernanceType value: {data!r}")
    return cast(GovernanceType, data)
