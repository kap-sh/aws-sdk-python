"""Generated from Smithy shape ``com.amazonaws.securityir#OptInFeatureName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

OptInFeatureName: TypeAlias = Literal["Triage",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Triage",))


def serialize_json(value: OptInFeatureName) -> str:
    return value


def deserialize_json(data: str) -> OptInFeatureName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OptInFeatureName value: {data!r}")
    return cast(OptInFeatureName, data)
