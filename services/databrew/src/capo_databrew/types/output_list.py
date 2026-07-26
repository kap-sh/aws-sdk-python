"""Generated from Smithy shape ``com.amazonaws.databrew#OutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.output

OutputList: TypeAlias = list["capo_databrew.types.output.Output"]


# --- restJson1 ser/de ---
def serialize_json(value: OutputList) -> list:
    import capo_databrew.types.output

    out: list = []
    for item in value:
        out.append(capo_databrew.types.output.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputList:
    import capo_databrew.types.output

    out: OutputList = []
    for item in data:
        out.append(capo_databrew.types.output.deserialize_json(item))
    return out
