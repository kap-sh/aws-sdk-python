"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterConfigMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterConfigMode: TypeAlias = Literal[
    "Enable",
    "Disable",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enable",
        "Disable",
    )
)


def serialize_aws_json_1_1(value: ClusterConfigMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterConfigMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterConfigMode value: {data!r}")
    return cast(ClusterConfigMode, data)
