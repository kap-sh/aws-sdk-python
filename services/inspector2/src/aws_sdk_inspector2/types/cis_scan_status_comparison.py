"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanStatusComparison``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisScanStatusComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EQUALS",))


def serialize_json(value: CisScanStatusComparison) -> str:
    return value


def deserialize_json(data: str) -> CisScanStatusComparison:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisScanStatusComparison value: {data!r}")
    return cast(CisScanStatusComparison, data)
