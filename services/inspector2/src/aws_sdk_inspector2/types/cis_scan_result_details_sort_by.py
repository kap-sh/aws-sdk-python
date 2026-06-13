"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanResultDetailsSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisScanResultDetailsSortBy: TypeAlias = Literal[
    "CHECK_ID",
    "STATUS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHECK_ID",
        "STATUS",
    )
)


def serialize_json(value: CisScanResultDetailsSortBy) -> str:
    return value


def deserialize_json(data: str) -> CisScanResultDetailsSortBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CisScanResultDetailsSortBy value: {data!r}"
        )
    return cast(CisScanResultDetailsSortBy, data)
