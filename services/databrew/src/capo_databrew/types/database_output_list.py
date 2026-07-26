"""Generated from Smithy shape ``com.amazonaws.databrew#DatabaseOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.database_output

DatabaseOutputList: TypeAlias = list[
    "capo_databrew.types.database_output.DatabaseOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseOutputList) -> list:
    import capo_databrew.types.database_output

    out: list = []
    for item in value:
        out.append(capo_databrew.types.database_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatabaseOutputList:
    import capo_databrew.types.database_output

    out: DatabaseOutputList = []
    for item in data:
        out.append(capo_databrew.types.database_output.deserialize_json(item))
    return out
