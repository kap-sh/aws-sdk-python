"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Parquet``."""

from typing_extensions import TypedDict


class Parquet(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: Parquet) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> Parquet:
    out: Parquet = {}  # type: ignore[typeddict-item]
    return out
