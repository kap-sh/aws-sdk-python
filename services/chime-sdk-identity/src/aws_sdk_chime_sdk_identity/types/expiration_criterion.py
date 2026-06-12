"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ExpirationCriterion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_identity.errors import DeserializationError

ExpirationCriterion: TypeAlias = Literal["CREATED_TIMESTAMP",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATED_TIMESTAMP",))


def serialize_json(value: ExpirationCriterion) -> str:
    return value


def deserialize_json(data: str) -> ExpirationCriterion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExpirationCriterion value: {data!r}")
    return cast(ExpirationCriterion, data)
