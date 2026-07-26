"""Generated from Smithy shape ``com.amazonaws.kendra#EntityPersonaConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.entity_persona_configuration

EntityPersonaConfigurationList: TypeAlias = list[
    "capo_kendra.types.entity_persona_configuration.EntityPersonaConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityPersonaConfigurationList) -> list:
    import capo_kendra.types.entity_persona_configuration

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.entity_persona_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntityPersonaConfigurationList:
    import capo_kendra.types.entity_persona_configuration

    out: EntityPersonaConfigurationList = []
    for item in data:
        out.append(
            capo_kendra.types.entity_persona_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
