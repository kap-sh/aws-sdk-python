"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingStatisticType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

FindingStatisticType: TypeAlias = Literal["COUNT_BY_SEVERITY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("COUNT_BY_SEVERITY",))


def serialize_json(value: FindingStatisticType) -> str:
    return value


def deserialize_json(data: str) -> FindingStatisticType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FindingStatisticType value: {data!r}")
    return cast(FindingStatisticType, data)
