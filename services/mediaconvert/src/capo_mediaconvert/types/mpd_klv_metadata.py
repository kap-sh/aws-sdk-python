"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MpdKlvMetadata``."""

from typing import Literal, TypeAlias, cast

"""To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and writes each instance to a separate event message box in the output, according to MISB ST1910.1. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank."""
MpdKlvMetadata: TypeAlias = Literal[
    "NONE",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: MpdKlvMetadata) -> str:
    return value


def deserialize_json(data: str) -> MpdKlvMetadata:
    return cast(MpdKlvMetadata, data)
