"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#NamespaceDeletionStatusErrorCodes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

NamespaceDeletionStatusErrorCodes: TypeAlias = Literal["VALIDATION_FAILED",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("VALIDATION_FAILED",))


def serialize_aws_json_1_1(value: NamespaceDeletionStatusErrorCodes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NamespaceDeletionStatusErrorCodes:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NamespaceDeletionStatusErrorCodes value: {data!r}"
        )
    return cast(NamespaceDeletionStatusErrorCodes, data)
