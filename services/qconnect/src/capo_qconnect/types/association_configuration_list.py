"""Generated from Smithy shape ``com.amazonaws.qconnect#AssociationConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.association_configuration

AssociationConfigurationList: TypeAlias = list[
    "capo_qconnect.types.association_configuration.AssociationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationConfigurationList) -> list:
    import capo_qconnect.types.association_configuration

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.association_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociationConfigurationList:
    import capo_qconnect.types.association_configuration

    out: AssociationConfigurationList = []
    for item in data:
        out.append(capo_qconnect.types.association_configuration.deserialize_json(item))
    return out
