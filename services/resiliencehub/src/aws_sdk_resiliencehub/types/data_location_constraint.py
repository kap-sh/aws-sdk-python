"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DataLocationConstraint``."""

from typing import Literal, TypeAlias, cast

DataLocationConstraint: TypeAlias = Literal[
    "AnyLocation",
    "SameContinent",
    "SameCountry",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataLocationConstraint) -> str:
    return value


def deserialize_json(data: str) -> DataLocationConstraint:
    return cast(DataLocationConstraint, data)
