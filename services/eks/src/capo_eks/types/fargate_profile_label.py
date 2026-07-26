"""Generated from Smithy shape ``com.amazonaws.eks#FargateProfileLabel``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.string

FargateProfileLabel: TypeAlias = dict[
    "capo_eks.types.string.String", "capo_eks.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FargateProfileLabel) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FargateProfileLabel:
    out: FargateProfileLabel = {}
    for key, value in data.items():
        out[key] = value
    return out
