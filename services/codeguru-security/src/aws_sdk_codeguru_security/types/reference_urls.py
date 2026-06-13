"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ReferenceUrls``."""

from typing import TypeAlias

ReferenceUrls: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceUrls) -> list:
    return list(value)


def deserialize_json(data: list) -> ReferenceUrls:
    return list(data)
