"""Generated from Smithy shape ``com.amazonaws.medialive#H265Level``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Level"""
H265Level: TypeAlias = Literal[
    "H265_LEVEL_1",
    "H265_LEVEL_2",
    "H265_LEVEL_2_1",
    "H265_LEVEL_3",
    "H265_LEVEL_3_1",
    "H265_LEVEL_4",
    "H265_LEVEL_4_1",
    "H265_LEVEL_5",
    "H265_LEVEL_5_1",
    "H265_LEVEL_5_2",
    "H265_LEVEL_6",
    "H265_LEVEL_6_1",
    "H265_LEVEL_6_2",
    "H265_LEVEL_AUTO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "H265_LEVEL_1",
        "H265_LEVEL_2",
        "H265_LEVEL_2_1",
        "H265_LEVEL_3",
        "H265_LEVEL_3_1",
        "H265_LEVEL_4",
        "H265_LEVEL_4_1",
        "H265_LEVEL_5",
        "H265_LEVEL_5_1",
        "H265_LEVEL_5_2",
        "H265_LEVEL_6",
        "H265_LEVEL_6_1",
        "H265_LEVEL_6_2",
        "H265_LEVEL_AUTO",
    )
)


def serialize_json(value: H265Level) -> str:
    return value


def deserialize_json(data: str) -> H265Level:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265Level value: {data!r}")
    return cast(H265Level, data)
