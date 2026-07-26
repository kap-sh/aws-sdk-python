"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmfcKlvMetadata``."""

from typing import Literal, TypeAlias, cast

"""To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank."""
CmfcKlvMetadata: TypeAlias = Literal[
    "PASSTHROUGH",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmfcKlvMetadata) -> str:
    return value


def deserialize_json(data: str) -> CmfcKlvMetadata:
    return cast(CmfcKlvMetadata, data)
