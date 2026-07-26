"""Generated from Smithy shape ``com.amazonaws.synthetics#Canaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.canary

Canaries: TypeAlias = list["capo_synthetics.types.canary.Canary"]


# --- restJson1 ser/de ---
def serialize_json(value: Canaries) -> list:
    import capo_synthetics.types.canary

    out: list = []
    for item in value:
        out.append(capo_synthetics.types.canary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Canaries:
    import capo_synthetics.types.canary

    out: Canaries = []
    for item in data:
        out.append(capo_synthetics.types.canary.deserialize_json(item))
    return out
