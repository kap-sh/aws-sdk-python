"""Generated from Smithy shape ``com.amazonaws.drs#NetworkInterfaces``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.network_interface

NetworkInterfaces: TypeAlias = list["capo_drs.types.network_interface.NetworkInterface"]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterfaces) -> list:
    import capo_drs.types.network_interface

    out: list = []
    for item in value:
        out.append(capo_drs.types.network_interface.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkInterfaces:
    import capo_drs.types.network_interface

    out: NetworkInterfaces = []
    for item in data:
        out.append(capo_drs.types.network_interface.deserialize_json(item))
    return out
