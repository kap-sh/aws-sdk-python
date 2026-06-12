"""Generated from Smithy shape ``com.amazonaws.medialive#SmoothGroupSparseTrackType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Smooth Group Sparse Track Type"""
SmoothGroupSparseTrackType: TypeAlias = Literal[
    "NONE",
    "SCTE_35",
    "SCTE_35_WITHOUT_SEGMENTATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SCTE_35",
        "SCTE_35_WITHOUT_SEGMENTATION",
    )
)


def serialize_json(value: SmoothGroupSparseTrackType) -> str:
    return value


def deserialize_json(data: str) -> SmoothGroupSparseTrackType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SmoothGroupSparseTrackType value: {data!r}"
        )
    return cast(SmoothGroupSparseTrackType, data)
