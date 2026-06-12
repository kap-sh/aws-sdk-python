"""Generated from Smithy shape ``com.amazonaws.connect#NextContactType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

NextContactType: TypeAlias = Literal["QUICK_CONNECT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("QUICK_CONNECT",))


def serialize_json(value: NextContactType) -> str:
    return value


def deserialize_json(data: str) -> NextContactType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NextContactType value: {data!r}")
    return cast(NextContactType, data)
