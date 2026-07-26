"""Generated from Smithy shape ``com.amazonaws.mgn#Cpus``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.cpu

Cpus: TypeAlias = list["capo_mgn.types.cpu.CPU"]


# --- restJson1 ser/de ---
def serialize_json(value: Cpus) -> list:
    import capo_mgn.types.cpu

    out: list = []
    for item in value:
        out.append(capo_mgn.types.cpu.serialize_json(item))
    return out


def deserialize_json(data: list) -> Cpus:
    import capo_mgn.types.cpu

    out: Cpus = []
    for item in data:
        out.append(capo_mgn.types.cpu.deserialize_json(item))
    return out
