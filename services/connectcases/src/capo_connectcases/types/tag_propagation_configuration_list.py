"""Generated from Smithy shape ``com.amazonaws.connectcases#TagPropagationConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.tag_propagation_configuration

TagPropagationConfigurationList: TypeAlias = list[
    "capo_connectcases.types.tag_propagation_configuration.TagPropagationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: TagPropagationConfigurationList) -> list:
    import capo_connectcases.types.tag_propagation_configuration

    out: list = []
    for item in value:
        out.append(
            capo_connectcases.types.tag_propagation_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TagPropagationConfigurationList:
    import capo_connectcases.types.tag_propagation_configuration

    out: TagPropagationConfigurationList = []
    for item in data:
        out.append(
            capo_connectcases.types.tag_propagation_configuration.deserialize_json(item)
        )
    return out
