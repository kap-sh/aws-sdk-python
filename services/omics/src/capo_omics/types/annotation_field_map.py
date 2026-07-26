"""Generated from Smithy shape ``com.amazonaws.omics#AnnotationFieldMap``."""

from typing import TypeAlias

AnnotationFieldMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AnnotationFieldMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AnnotationFieldMap:
    out: AnnotationFieldMap = {}
    for key, value in data.items():
        out[key] = value
    return out
