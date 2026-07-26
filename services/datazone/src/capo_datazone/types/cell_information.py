"""Generated from Smithy shape ``com.amazonaws.datazone#CellInformation``."""

from typing_extensions import TypedDict


class CellInformation(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CellInformation) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CellInformation:
    out: CellInformation = {}  # type: ignore[typeddict-item]
    return out
