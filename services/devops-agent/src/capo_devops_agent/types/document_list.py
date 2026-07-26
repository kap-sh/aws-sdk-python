"""Generated from Smithy shape ``com.amazonaws.devopsagent#DocumentList``."""

from typing import TypeAlias

DocumentList: TypeAlias = list["object"]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentList) -> list:
    return list(value)


def deserialize_json(data: list) -> DocumentList:
    return list(data)
