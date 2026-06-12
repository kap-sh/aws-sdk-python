"""Generated from Smithy shape ``com.amazonaws.fsx#InputOntapVolumeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

InputOntapVolumeType: TypeAlias = Literal[
    "RW",
    "DP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RW",
        "DP",
    )
)


def serialize_aws_json_1_1(value: InputOntapVolumeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputOntapVolumeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputOntapVolumeType value: {data!r}")
    return cast(InputOntapVolumeType, data)
