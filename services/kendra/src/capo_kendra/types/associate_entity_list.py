"""Generated from Smithy shape ``com.amazonaws.kendra#AssociateEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.entity_configuration

AssociateEntityList: TypeAlias = list[
    "capo_kendra.types.entity_configuration.EntityConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateEntityList) -> list:
    import capo_kendra.types.entity_configuration

    out: list = []
    for item in value:
        out.append(capo_kendra.types.entity_configuration.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssociateEntityList:
    import capo_kendra.types.entity_configuration

    out: AssociateEntityList = []
    for item in data:
        out.append(
            capo_kendra.types.entity_configuration.deserialize_aws_json_1_1(item)
        )
    return out
