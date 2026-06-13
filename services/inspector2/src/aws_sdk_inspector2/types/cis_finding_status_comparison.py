"""Generated from Smithy shape ``com.amazonaws.inspector2#CisFindingStatusComparison``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisFindingStatusComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EQUALS",))


def serialize_json(value: CisFindingStatusComparison) -> str:
    return value


def deserialize_json(data: str) -> CisFindingStatusComparison:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CisFindingStatusComparison value: {data!r}"
        )
    return cast(CisFindingStatusComparison, data)
