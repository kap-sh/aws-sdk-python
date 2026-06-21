"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MpdScte35Esam``."""

from typing import Literal, TypeAlias, cast

"""Use this setting only when you specify SCTE-35 markers from ESAM. Choose INSERT to put SCTE-35 markers in this output at the insertion points that you specify in an ESAM XML document. Provide the document in the setting SCC XML."""
MpdScte35Esam: TypeAlias = Literal[
    "INSERT",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MpdScte35Esam) -> str:
    return value


def deserialize_json(data: str) -> MpdScte35Esam:
    return cast(MpdScte35Esam, data)
