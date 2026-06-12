"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlProperty``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

SecurityControlProperty: TypeAlias = Literal["Parameters",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Parameters",))


def serialize_json(value: SecurityControlProperty) -> str:
    return value


def deserialize_json(data: str) -> SecurityControlProperty:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SecurityControlProperty value: {data!r}")
    return cast(SecurityControlProperty, data)
