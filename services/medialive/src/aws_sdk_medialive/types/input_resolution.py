"""Generated from Smithy shape ``com.amazonaws.medialive#InputResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Input resolution based on lines of vertical resolution in the input; SD is less than 720 lines, HD is 720 to 1080 lines, UHD is greater than 1080 lines"""
InputResolution: TypeAlias = Literal[
    "SD",
    "HD",
    "UHD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SD",
        "HD",
        "UHD",
    )
)


def serialize_json(value: InputResolution) -> str:
    return value


def deserialize_json(data: str) -> InputResolution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputResolution value: {data!r}")
    return cast(InputResolution, data)
