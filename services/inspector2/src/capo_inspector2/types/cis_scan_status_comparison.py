"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanStatusComparison``."""

from typing import Literal, TypeAlias, cast

CisScanStatusComparison: TypeAlias = Literal["EQUALS",]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanStatusComparison) -> str:
    return value


def deserialize_json(data: str) -> CisScanStatusComparison:
    return cast(CisScanStatusComparison, data)
