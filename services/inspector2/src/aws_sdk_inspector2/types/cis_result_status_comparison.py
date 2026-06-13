"""Generated from Smithy shape ``com.amazonaws.inspector2#CisResultStatusComparison``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisResultStatusComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EQUALS",))


def serialize_json(value: CisResultStatusComparison) -> str:
    return value


def deserialize_json(data: str) -> CisResultStatusComparison:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisResultStatusComparison value: {data!r}")
    return cast(CisResultStatusComparison, data)
