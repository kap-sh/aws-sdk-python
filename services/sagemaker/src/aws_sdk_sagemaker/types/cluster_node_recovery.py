"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterNodeRecovery``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterNodeRecovery: TypeAlias = Literal[
    "Automatic",
    "None",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Automatic",
        "None",
    )
)


def serialize_aws_json_1_1(value: ClusterNodeRecovery) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterNodeRecovery:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterNodeRecovery value: {data!r}")
    return cast(ClusterNodeRecovery, data)
