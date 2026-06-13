"""Generated from Smithy shape ``com.amazonaws.emr#ProfilerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

ProfilerType: TypeAlias = Literal[
    "SHS",
    "TEZUI",
    "YTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHS",
        "TEZUI",
        "YTS",
    )
)


def serialize_aws_json_1_1(value: ProfilerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProfilerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfilerType value: {data!r}")
    return cast(ProfilerType, data)
