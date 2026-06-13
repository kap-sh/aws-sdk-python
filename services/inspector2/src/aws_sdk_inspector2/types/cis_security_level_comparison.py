"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSecurityLevelComparison``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisSecurityLevelComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EQUALS",))


def serialize_json(value: CisSecurityLevelComparison) -> str:
    return value


def deserialize_json(data: str) -> CisSecurityLevelComparison:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CisSecurityLevelComparison value: {data!r}"
        )
    return cast(CisSecurityLevelComparison, data)
