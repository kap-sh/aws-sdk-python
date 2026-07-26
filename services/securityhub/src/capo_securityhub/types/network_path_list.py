"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkPathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.network_path_component

NetworkPathList: TypeAlias = list[
    "capo_securityhub.types.network_path_component.NetworkPathComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkPathList) -> list:
    import capo_securityhub.types.network_path_component

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.network_path_component.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkPathList:
    import capo_securityhub.types.network_path_component

    out: NetworkPathList = []
    for item in data:
        out.append(capo_securityhub.types.network_path_component.deserialize_json(item))
    return out
