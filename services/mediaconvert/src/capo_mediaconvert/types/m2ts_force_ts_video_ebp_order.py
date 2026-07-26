"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsForceTsVideoEbpOrder``."""

from typing import Literal, TypeAlias, cast

"""Keep the default value unless you know that your audio EBP markers are incorrectly appearing before your video EBP markers. To correct this problem, set this value to Force."""
M2tsForceTsVideoEbpOrder: TypeAlias = Literal[
    "FORCE",
    "DEFAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsForceTsVideoEbpOrder) -> str:
    return value


def deserialize_json(data: str) -> M2tsForceTsVideoEbpOrder:
    return cast(M2tsForceTsVideoEbpOrder, data)
