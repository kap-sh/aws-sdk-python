"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaUrlWithSuffixExample``."""

from typing import TypeAlias

MetaUrlWithSuffixExample: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MetaUrlWithSuffixExample) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MetaUrlWithSuffixExample:
    out: MetaUrlWithSuffixExample = {}
    for key, value in data.items():
        out[key] = value
    return out
