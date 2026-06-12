"""Generated from Smithy shape ``com.amazonaws.fsx#VolumeStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

VolumeStyle: TypeAlias = Literal[
    "FLEXVOL",
    "FLEXGROUP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FLEXVOL",
        "FLEXGROUP",
    )
)


def serialize_aws_json_1_1(value: VolumeStyle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VolumeStyle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VolumeStyle value: {data!r}")
    return cast(VolumeStyle, data)
