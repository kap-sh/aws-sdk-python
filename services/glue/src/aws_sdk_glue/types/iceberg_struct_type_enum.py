"""Generated from Smithy shape ``com.amazonaws.glue#IcebergStructTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

IcebergStructTypeEnum: TypeAlias = Literal["struct",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("struct",))


def serialize_aws_json_1_1(value: IcebergStructTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IcebergStructTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IcebergStructTypeEnum value: {data!r}")
    return cast(IcebergStructTypeEnum, data)
