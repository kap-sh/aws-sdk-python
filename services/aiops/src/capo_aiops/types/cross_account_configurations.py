"""Generated from Smithy shape ``com.amazonaws.aiops#CrossAccountConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_aiops.types.cross_account_configuration

CrossAccountConfigurations: TypeAlias = list[
    "capo_aiops.types.cross_account_configuration.CrossAccountConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CrossAccountConfigurations) -> list:
    import capo_aiops.types.cross_account_configuration

    out: list = []
    for item in value:
        out.append(capo_aiops.types.cross_account_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> CrossAccountConfigurations:
    import capo_aiops.types.cross_account_configuration

    out: CrossAccountConfigurations = []
    for item in data:
        out.append(capo_aiops.types.cross_account_configuration.deserialize_json(item))
    return out
