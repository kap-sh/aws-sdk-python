"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSlurmNodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterSlurmNodeType: TypeAlias = Literal[
    "Controller",
    "Login",
    "Compute",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Controller",
        "Login",
        "Compute",
    )
)


def serialize_aws_json_1_1(value: ClusterSlurmNodeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterSlurmNodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterSlurmNodeType value: {data!r}")
    return cast(ClusterSlurmNodeType, data)
