"""Generated from Smithy shape ``com.amazonaws.synthetics#Dependencies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_synthetics.types.dependency

Dependencies: TypeAlias = list["capo_synthetics.types.dependency.Dependency"]


# --- restJson1 ser/de ---
def serialize_json(value: Dependencies) -> list:
    import capo_synthetics.types.dependency

    out: list = []
    for item in value:
        out.append(capo_synthetics.types.dependency.serialize_json(item))
    return out


def deserialize_json(data: list) -> Dependencies:
    import capo_synthetics.types.dependency

    out: Dependencies = []
    for item in data:
        out.append(capo_synthetics.types.dependency.deserialize_json(item))
    return out
