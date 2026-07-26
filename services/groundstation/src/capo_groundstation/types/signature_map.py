"""Generated from Smithy shape ``com.amazonaws.groundstation#SignatureMap``."""

from typing import TypeAlias

SignatureMap: TypeAlias = dict["str", "bool"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SignatureMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SignatureMap:
    out: SignatureMap = {}
    for key, value in data.items():
        out[key] = value
    return out
