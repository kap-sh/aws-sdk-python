"""Generated from Smithy shape ``com.amazonaws.fsx#OntapVolumeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

OntapVolumeType: TypeAlias = Literal[
    "RW",
    "DP",
    "LS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RW",
        "DP",
        "LS",
    )
)


def serialize_aws_json_1_1(value: OntapVolumeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OntapVolumeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OntapVolumeType value: {data!r}")
    return cast(OntapVolumeType, data)
