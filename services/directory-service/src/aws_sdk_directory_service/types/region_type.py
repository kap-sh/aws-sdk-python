"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

RegionType: TypeAlias = Literal[
    "Primary",
    "Additional",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Primary",
        "Additional",
    )
)


def serialize_aws_json_1_1(value: RegionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegionType value: {data!r}")
    return cast(RegionType, data)
