"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NielsenActiveWatermarkProcessType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose the type of Nielsen watermarks that you want in your outputs. When you choose NAES 2 and NW, you must provide a value for the setting SID. When you choose CBET, you must provide a value for the setting CSID. When you choose NAES 2, NW, and CBET, you must provide values for both of these settings."""
NielsenActiveWatermarkProcessType: TypeAlias = Literal[
    "NAES2_AND_NW",
    "CBET",
    "NAES2_AND_NW_AND_CBET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAES2_AND_NW",
        "CBET",
        "NAES2_AND_NW_AND_CBET",
    )
)


def serialize_json(value: NielsenActiveWatermarkProcessType) -> str:
    return value


def deserialize_json(data: str) -> NielsenActiveWatermarkProcessType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NielsenActiveWatermarkProcessType value: {data!r}"
        )
    return cast(NielsenActiveWatermarkProcessType, data)
