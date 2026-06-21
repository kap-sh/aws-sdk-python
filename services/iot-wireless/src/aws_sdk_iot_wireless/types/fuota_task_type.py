"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTaskType``."""

from typing import Literal, TypeAlias, cast

"""<p>The FUOTA task type.</p>"""
FuotaTaskType: TypeAlias = Literal["LoRaWAN",]


# --- restJson1 ser/de ---
def serialize_json(value: FuotaTaskType) -> str:
    return value


def deserialize_json(data: str) -> FuotaTaskType:
    return cast(FuotaTaskType, data)
