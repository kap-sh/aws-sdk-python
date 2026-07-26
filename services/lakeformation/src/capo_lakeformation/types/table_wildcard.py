"""Generated from Smithy shape ``com.amazonaws.lakeformation#TableWildcard``."""

from typing_extensions import TypedDict


class TableWildcard(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: TableWildcard) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> TableWildcard:
    out: TableWildcard = {}  # type: ignore[typeddict-item]
    return out
