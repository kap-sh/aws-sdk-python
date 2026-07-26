"""Generated from Smithy shape ``com.amazonaws.backup#ScanFinding``."""

from typing import Literal, TypeAlias, cast

ScanFinding: TypeAlias = Literal["MALWARE",]


# --- restJson1 ser/de ---
def serialize_json(value: ScanFinding) -> str:
    return value


def deserialize_json(data: str) -> ScanFinding:
    return cast(ScanFinding, data)
