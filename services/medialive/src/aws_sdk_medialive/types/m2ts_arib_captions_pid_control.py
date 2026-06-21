"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsAribCaptionsPidControl``."""

from typing import Literal, TypeAlias, cast

"""M2ts Arib Captions Pid Control"""
M2tsAribCaptionsPidControl: TypeAlias = Literal[
    "AUTO",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsAribCaptionsPidControl) -> str:
    return value


def deserialize_json(data: str) -> M2tsAribCaptionsPidControl:
    return cast(M2tsAribCaptionsPidControl, data)
