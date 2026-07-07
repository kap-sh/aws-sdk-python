"""Generated from Smithy shape ``com.amazonaws.datazone#AllUsersGrantFilter``."""

from typing_extensions import TypedDict


class AllUsersGrantFilter(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AllUsersGrantFilter) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AllUsersGrantFilter:
    out: AllUsersGrantFilter = {}  # type: ignore[typeddict-item]
    return out
