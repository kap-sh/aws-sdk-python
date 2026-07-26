"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfSchemaChangeDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.schema_change_details

ListOfSchemaChangeDetails: TypeAlias = list[
    "capo_dataexchange.types.schema_change_details.SchemaChangeDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfSchemaChangeDetails) -> list:
    import capo_dataexchange.types.schema_change_details

    out: list = []
    for item in value:
        out.append(capo_dataexchange.types.schema_change_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfSchemaChangeDetails:
    import capo_dataexchange.types.schema_change_details

    out: ListOfSchemaChangeDetails = []
    for item in data:
        out.append(capo_dataexchange.types.schema_change_details.deserialize_json(item))
    return out
