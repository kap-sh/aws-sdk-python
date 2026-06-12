"""Generated from Smithy shape ``com.amazonaws.glue#HyperTargetCompressionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

HyperTargetCompressionType: TypeAlias = Literal["uncompressed",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("uncompressed",))


def serialize_aws_json_1_1(value: HyperTargetCompressionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperTargetCompressionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HyperTargetCompressionType value: {data!r}"
        )
    return cast(HyperTargetCompressionType, data)
