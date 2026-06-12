"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardVersionSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelCardVersionSortBy: TypeAlias = Literal["Version",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Version",))


def serialize_aws_json_1_1(value: ModelCardVersionSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardVersionSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCardVersionSortBy value: {data!r}")
    return cast(ModelCardVersionSortBy, data)
