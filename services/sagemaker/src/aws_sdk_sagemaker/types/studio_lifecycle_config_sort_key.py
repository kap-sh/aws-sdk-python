"""Generated from Smithy shape ``com.amazonaws.sagemaker#StudioLifecycleConfigSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

StudioLifecycleConfigSortKey: TypeAlias = Literal[
    "CreationTime",
    "LastModifiedTime",
    "Name",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreationTime",
        "LastModifiedTime",
        "Name",
    )
)


def serialize_aws_json_1_1(value: StudioLifecycleConfigSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StudioLifecycleConfigSortKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StudioLifecycleConfigSortKey value: {data!r}"
        )
    return cast(StudioLifecycleConfigSortKey, data)
