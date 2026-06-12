"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortArtifactsBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortArtifactsBy: TypeAlias = Literal["CreationTime",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CreationTime",))


def serialize_aws_json_1_1(value: SortArtifactsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortArtifactsBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortArtifactsBy value: {data!r}")
    return cast(SortArtifactsBy, data)
