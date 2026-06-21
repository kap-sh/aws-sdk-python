"""Generated from Smithy shape ``com.amazonaws.textract#ValueType``."""

from typing import Literal, TypeAlias, cast

ValueType: TypeAlias = Literal["DATE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValueType:
    return cast(ValueType, data)
