"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductRevisions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_product_revision

DataProductRevisions: TypeAlias = list[
    "aws_sdk_datazone.types.data_product_revision.DataProductRevision"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataProductRevisions) -> list:
    import aws_sdk_datazone.types.data_product_revision

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.data_product_revision.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataProductRevisions:
    import aws_sdk_datazone.types.data_product_revision

    out: DataProductRevisions = []
    for item in data:
        out.append(aws_sdk_datazone.types.data_product_revision.deserialize_json(item))
    return out
