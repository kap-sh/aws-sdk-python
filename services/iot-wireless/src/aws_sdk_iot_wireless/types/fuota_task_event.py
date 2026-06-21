"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaTaskEvent``."""

from typing import Literal, TypeAlias, cast

"""<p>The event for a log message, if the log message is tied to a FUOTA task.</p>"""
FuotaTaskEvent: TypeAlias = Literal["Fuota",]


# --- restJson1 ser/de ---
def serialize_json(value: FuotaTaskEvent) -> str:
    return value


def deserialize_json(data: str) -> FuotaTaskEvent:
    return cast(FuotaTaskEvent, data)
