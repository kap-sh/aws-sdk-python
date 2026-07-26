"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTaskStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a FUOTA task.</p>"""
FuotaTaskStatus: TypeAlias = Literal[
    "Pending",
    "FuotaSession_Waiting",
    "In_FuotaSession",
    "FuotaDone",
    "Delete_Waiting",
]


# --- restJson1 ser/de ---
def serialize_json(value: FuotaTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> FuotaTaskStatus:
    return cast(FuotaTaskStatus, data)
