"""Generated from Smithy shape ``com.amazonaws.ecs#EBSResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

EBSResourceType: TypeAlias = Literal["volume",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("volume",))


def serialize_aws_json_1_1(value: EBSResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EBSResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EBSResourceType value: {data!r}")
    return cast(EBSResourceType, data)
