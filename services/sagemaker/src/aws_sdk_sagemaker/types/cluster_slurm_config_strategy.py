"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSlurmConfigStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterSlurmConfigStrategy: TypeAlias = Literal[
    "Overwrite",
    "Managed",
    "Merge",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Overwrite",
        "Managed",
        "Merge",
    )
)


def serialize_aws_json_1_1(value: ClusterSlurmConfigStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterSlurmConfigStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ClusterSlurmConfigStrategy value: {data!r}"
        )
    return cast(ClusterSlurmConfigStrategy, data)
