"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListVectorsOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3vectors.types.list_output_vector

ListVectorsOutputList: TypeAlias = list[
    "capo_s3vectors.types.list_output_vector.ListOutputVector"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorsOutputList) -> list:
    import capo_s3vectors.types.list_output_vector

    out: list = []
    for item in value:
        out.append(capo_s3vectors.types.list_output_vector.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListVectorsOutputList:
    import capo_s3vectors.types.list_output_vector

    out: ListVectorsOutputList = []
    for item in data:
        out.append(capo_s3vectors.types.list_output_vector.deserialize_json(item))
    return out
