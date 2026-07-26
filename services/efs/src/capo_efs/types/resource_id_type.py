"""Generated from Smithy shape ``com.amazonaws.efs#ResourceIdType``."""

from typing import Literal, TypeAlias, cast

"""A preference indicating a choice to use 63bit/32bit IDs for all applicable resources."""
ResourceIdType: TypeAlias = Literal[
    "LONG_ID",
    "SHORT_ID",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceIdType) -> str:
    return value


def deserialize_json(data: str) -> ResourceIdType:
    return cast(ResourceIdType, data)
