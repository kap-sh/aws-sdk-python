"""Generated from Smithy shape ``com.amazonaws.backup#ScanFinding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

ScanFinding: TypeAlias = Literal["MALWARE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MALWARE",))


def serialize_json(value: ScanFinding) -> str:
    return value


def deserialize_json(data: str) -> ScanFinding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanFinding value: {data!r}")
    return cast(ScanFinding, data)
