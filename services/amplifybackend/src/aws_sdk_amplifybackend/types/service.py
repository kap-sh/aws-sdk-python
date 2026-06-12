"""Generated from Smithy shape ``com.amazonaws.amplifybackend#Service``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

Service: TypeAlias = Literal["COGNITO",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("COGNITO",))


def serialize_json(value: Service) -> str:
    return value


def deserialize_json(data: str) -> Service:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Service value: {data!r}")
    return cast(Service, data)
