"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductRevisions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.data_product_revision

DataProductRevisions: TypeAlias = list[
    "capo_datazone.types.data_product_revision.DataProductRevision"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataProductRevisions) -> list:
    import capo_datazone.types.data_product_revision

    out: list = []
    for item in value:
        out.append(capo_datazone.types.data_product_revision.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataProductRevisions:
    import capo_datazone.types.data_product_revision

    out: DataProductRevisions = []
    for item in data:
        out.append(capo_datazone.types.data_product_revision.deserialize_json(item))
    return out
