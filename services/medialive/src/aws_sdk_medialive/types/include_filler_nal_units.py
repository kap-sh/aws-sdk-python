"""Generated from Smithy shape ``com.amazonaws.medialive#IncludeFillerNalUnits``."""

from typing import Literal, TypeAlias, cast

"""Include Filler Nal Units"""
IncludeFillerNalUnits: TypeAlias = Literal[
    "AUTO",
    "DROP",
    "INCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludeFillerNalUnits) -> str:
    return value


def deserialize_json(data: str) -> IncludeFillerNalUnits:
    return cast(IncludeFillerNalUnits, data)
