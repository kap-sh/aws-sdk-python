"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AppSortKey: TypeAlias = Literal["CreationTime",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CreationTime",))


def serialize_aws_json_1_1(value: AppSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppSortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppSortKey value: {data!r}")
    return cast(AppSortKey, data)
