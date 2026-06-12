"""Generated from Smithy shape ``com.amazonaws.ivs#ThumbnailConfigurationResolution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs.errors import DeserializationError

ThumbnailConfigurationResolution: TypeAlias = Literal[
    "SD",
    "HD",
    "FULL_HD",
    "LOWEST_RESOLUTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SD",
        "HD",
        "FULL_HD",
        "LOWEST_RESOLUTION",
    )
)


def serialize_json(value: ThumbnailConfigurationResolution) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailConfigurationResolution:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ThumbnailConfigurationResolution value: {data!r}"
        )
    return cast(ThumbnailConfigurationResolution, data)
