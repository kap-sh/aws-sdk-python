"""Generated from Smithy shape ``com.amazonaws.textract#ValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_textract.errors import DeserializationError

ValueType: TypeAlias = Literal["DATE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DATE",))


def serialize_aws_json_1_1(value: ValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValueType value: {data!r}")
    return cast(ValueType, data)
