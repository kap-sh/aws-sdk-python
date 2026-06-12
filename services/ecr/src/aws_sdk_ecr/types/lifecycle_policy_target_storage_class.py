"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyTargetStorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecr.errors import DeserializationError

LifecyclePolicyTargetStorageClass: TypeAlias = Literal["ARCHIVE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ARCHIVE",))


def serialize_aws_json_1_1(value: LifecyclePolicyTargetStorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecyclePolicyTargetStorageClass:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LifecyclePolicyTargetStorageClass value: {data!r}"
        )
    return cast(LifecyclePolicyTargetStorageClass, data)
