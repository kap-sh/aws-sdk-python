"""Generated from Smithy shape ``com.amazonaws.kendra#FeaturedResultsSetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

FeaturedResultsSetStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: FeaturedResultsSetStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeaturedResultsSetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FeaturedResultsSetStatus value: {data!r}")
    return cast(FeaturedResultsSetStatus, data)
