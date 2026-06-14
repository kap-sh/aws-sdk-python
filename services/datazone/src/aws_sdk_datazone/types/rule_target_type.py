"""Generated from Smithy shape ``com.amazonaws.datazone#RuleTargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

RuleTargetType: TypeAlias = Literal["DOMAIN_UNIT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DOMAIN_UNIT",))


def serialize_json(value: RuleTargetType) -> str:
    return value


def deserialize_json(data: str) -> RuleTargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleTargetType value: {data!r}")
    return cast(RuleTargetType, data)
