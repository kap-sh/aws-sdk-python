"""Generated from Smithy shape ``com.amazonaws.s3vectors#PutVectorsInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.put_input_vector

PutVectorsInputList: TypeAlias = list[
    "aws_sdk_s3vectors.types.put_input_vector.PutInputVector"
]


# --- restJson1 ser/de ---
def serialize_json(value: PutVectorsInputList) -> list:
    import aws_sdk_s3vectors.types.put_input_vector

    out: list = []
    for item in value:
        out.append(aws_sdk_s3vectors.types.put_input_vector.serialize_json(item))
    return out


def deserialize_json(data: list) -> PutVectorsInputList:
    import aws_sdk_s3vectors.types.put_input_vector

    out: PutVectorsInputList = []
    for item in data:
        out.append(aws_sdk_s3vectors.types.put_input_vector.deserialize_json(item))
    return out
