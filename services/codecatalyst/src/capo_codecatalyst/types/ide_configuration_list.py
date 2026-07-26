"""Generated from Smithy shape ``com.amazonaws.codecatalyst#IdeConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.ide_configuration

IdeConfigurationList: TypeAlias = list[
    "capo_codecatalyst.types.ide_configuration.IdeConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdeConfigurationList) -> list:
    import capo_codecatalyst.types.ide_configuration

    out: list = []
    for item in value:
        out.append(capo_codecatalyst.types.ide_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> IdeConfigurationList:
    import capo_codecatalyst.types.ide_configuration

    out: IdeConfigurationList = []
    for item in data:
        out.append(capo_codecatalyst.types.ide_configuration.deserialize_json(item))
    return out
