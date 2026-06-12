"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AccelerationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify whether the service runs your job with accelerated transcoding. Choose DISABLED if you don't want accelerated transcoding. Choose ENABLED if you want your job to run with accelerated transcoding and to fail if your input files or your job settings aren't compatible with accelerated transcoding. Choose PREFERRED if you want your job to run with accelerated transcoding if the job is compatible with the feature and to run at standard speed if it's not."""
AccelerationMode: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "PREFERRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
        "PREFERRED",
    )
)


def serialize_json(value: AccelerationMode) -> str:
    return value


def deserialize_json(data: str) -> AccelerationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccelerationMode value: {data!r}")
    return cast(AccelerationMode, data)
