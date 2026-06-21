"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultDetailsSortBy``."""

from typing import Literal, TypeAlias, cast

CisScanResultDetailsSortBy: TypeAlias = Literal[
    "CHECK_ID",
    "STATUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanResultDetailsSortBy) -> str:
    return value


def deserialize_json(data: str) -> CisScanResultDetailsSortBy:
    return cast(CisScanResultDetailsSortBy, data)
