"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PolicyExistenceCondition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

PolicyExistenceCondition: TypeAlias = Literal[
    "POLICY_MUST_EXIST",
    "POLICY_MUST_NOT_EXIST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POLICY_MUST_EXIST",
        "POLICY_MUST_NOT_EXIST",
    )
)


def serialize_json(value: PolicyExistenceCondition) -> str:
    return value


def deserialize_json(data: str) -> PolicyExistenceCondition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyExistenceCondition value: {data!r}")
    return cast(PolicyExistenceCondition, data)
