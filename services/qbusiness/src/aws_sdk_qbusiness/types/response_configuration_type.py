"""Generated from Smithy shape ``com.amazonaws.qbusiness#ResponseConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

ResponseConfigurationType: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALL",))


def serialize_json(value: ResponseConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> ResponseConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResponseConfigurationType value: {data!r}")
    return cast(ResponseConfigurationType, data)
