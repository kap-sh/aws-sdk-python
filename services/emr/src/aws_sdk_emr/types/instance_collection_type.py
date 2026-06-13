"""Generated from Smithy shape ``com.amazonaws.emr#InstanceCollectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

InstanceCollectionType: TypeAlias = Literal[
    "INSTANCE_FLEET",
    "INSTANCE_GROUP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSTANCE_FLEET",
        "INSTANCE_GROUP",
    )
)


def serialize_aws_json_1_1(value: InstanceCollectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceCollectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceCollectionType value: {data!r}")
    return cast(InstanceCollectionType, data)
