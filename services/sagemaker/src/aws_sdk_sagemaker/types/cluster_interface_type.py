"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInterfaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ClusterInterfaceType: TypeAlias = Literal[
    "efa",
    "efa-only",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "efa",
        "efa-only",
    )
)


def serialize_aws_json_1_1(value: ClusterInterfaceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterInterfaceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterInterfaceType value: {data!r}")
    return cast(ClusterInterfaceType, data)
