"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#KmsConstraintsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.kms_constraints_key
    import capo_accessanalyzer.types.kms_constraints_value

KmsConstraintsMap: TypeAlias = dict[
    "capo_accessanalyzer.types.kms_constraints_key.KmsConstraintsKey",
    "capo_accessanalyzer.types.kms_constraints_value.KmsConstraintsValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: KmsConstraintsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> KmsConstraintsMap:
    out: KmsConstraintsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
