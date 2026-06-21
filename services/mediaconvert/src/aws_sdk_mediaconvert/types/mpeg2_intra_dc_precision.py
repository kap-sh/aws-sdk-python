"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2IntraDcPrecision``."""

from typing import Literal, TypeAlias, cast

"""Use Intra DC precision to set quantization precision for intra-block DC coefficients. If you choose the value auto, the service will automatically select the precision based on the per-frame compression ratio."""
Mpeg2IntraDcPrecision: TypeAlias = Literal[
    "AUTO",
    "INTRA_DC_PRECISION_8",
    "INTRA_DC_PRECISION_9",
    "INTRA_DC_PRECISION_10",
    "INTRA_DC_PRECISION_11",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2IntraDcPrecision) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2IntraDcPrecision:
    return cast(Mpeg2IntraDcPrecision, data)
