"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceSharingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ResourceSharingStrategy: TypeAlias = Literal[
    "Lend",
    "DontLend",
    "LendAndBorrow",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Lend",
        "DontLend",
        "LendAndBorrow",
    )
)


def serialize_aws_json_1_1(value: ResourceSharingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceSharingStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceSharingStrategy value: {data!r}")
    return cast(ResourceSharingStrategy, data)
