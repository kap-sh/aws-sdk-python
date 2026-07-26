"""Generated from Smithy shape ``com.amazonaws.neptunedata#MlModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_neptunedata.types.ml_config_definition

MlModels: TypeAlias = list[
    "capo_neptunedata.types.ml_config_definition.MlConfigDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: MlModels) -> list:
    import capo_neptunedata.types.ml_config_definition

    out: list = []
    for item in value:
        out.append(capo_neptunedata.types.ml_config_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> MlModels:
    import capo_neptunedata.types.ml_config_definition

    out: MlModels = []
    for item in data:
        out.append(capo_neptunedata.types.ml_config_definition.deserialize_json(item))
    return out
