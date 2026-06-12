"""Generated from Smithy shape ``com.amazonaws.glue#TransformType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

TransformType: TypeAlias = Literal["FIND_MATCHES",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FIND_MATCHES",))


def serialize_aws_json_1_1(value: TransformType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransformType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransformType value: {data!r}")
    return cast(TransformType, data)
