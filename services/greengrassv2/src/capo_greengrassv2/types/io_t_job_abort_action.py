"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobAbortAction``."""

from typing import Literal, TypeAlias, cast

IoTJobAbortAction: TypeAlias = Literal["CANCEL",]


# --- restJson1 ser/de ---
def serialize_json(value: IoTJobAbortAction) -> str:
    return value


def deserialize_json(data: str) -> IoTJobAbortAction:
    return cast(IoTJobAbortAction, data)
