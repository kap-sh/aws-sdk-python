"""Generated from Smithy shape ``com.amazonaws.s3vectors#GetVectorsOutputList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.get_output_vector

GetVectorsOutputList: TypeAlias = list["aws_sdk_s3vectors.types.get_output_vector.GetOutputVector"]


# --- restJson1 ser/de ---
def serialize_json(value: GetVectorsOutputList) -> list:
    import aws_sdk_s3vectors.types.get_output_vector
    out: list = []
    for item in value:
        out.append(aws_sdk_s3vectors.types.get_output_vector.serialize_json(item))
    return out


def deserialize_json(data: list) -> GetVectorsOutputList:
    import aws_sdk_s3vectors.types.get_output_vector
    out: GetVectorsOutputList = []
    for item in data:
        out.append(aws_sdk_s3vectors.types.get_output_vector.deserialize_json(item))
    return out