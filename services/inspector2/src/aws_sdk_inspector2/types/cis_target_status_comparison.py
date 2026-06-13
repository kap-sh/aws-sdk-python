"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetStatusComparison``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisTargetStatusComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EQUALS",))


def serialize_json(value: CisTargetStatusComparison) -> str:
    return value


def deserialize_json(data: str) -> CisTargetStatusComparison:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisTargetStatusComparison value: {data!r}")
    return cast(CisTargetStatusComparison, data)
