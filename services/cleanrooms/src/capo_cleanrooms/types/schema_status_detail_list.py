"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaStatusDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.schema_status_detail

SchemaStatusDetailList: TypeAlias = list[
    "capo_cleanrooms.types.schema_status_detail.SchemaStatusDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaStatusDetailList) -> list:
    import capo_cleanrooms.types.schema_status_detail

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.schema_status_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchemaStatusDetailList:
    import capo_cleanrooms.types.schema_status_detail

    out: SchemaStatusDetailList = []
    for item in data:
        out.append(capo_cleanrooms.types.schema_status_detail.deserialize_json(item))
    return out
