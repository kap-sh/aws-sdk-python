"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenWatermarksDistributionTypes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Nielsen Watermarks Distribution Types"""
NielsenWatermarksDistributionTypes: TypeAlias = Literal[
    "FINAL_DISTRIBUTOR",
    "PROGRAM_CONTENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FINAL_DISTRIBUTOR",
        "PROGRAM_CONTENT",
    )
)


def serialize_json(value: NielsenWatermarksDistributionTypes) -> str:
    return value


def deserialize_json(data: str) -> NielsenWatermarksDistributionTypes:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NielsenWatermarksDistributionTypes value: {data!r}"
        )
    return cast(NielsenWatermarksDistributionTypes, data)
