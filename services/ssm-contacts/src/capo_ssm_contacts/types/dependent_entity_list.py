"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DependentEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_contacts.types.dependent_entity

DependentEntityList: TypeAlias = list[
    "capo_ssm_contacts.types.dependent_entity.DependentEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependentEntityList) -> list:
    import capo_ssm_contacts.types.dependent_entity

    out: list = []
    for item in value:
        out.append(
            capo_ssm_contacts.types.dependent_entity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DependentEntityList:
    import capo_ssm_contacts.types.dependent_entity

    out: DependentEntityList = []
    for item in data:
        out.append(
            capo_ssm_contacts.types.dependent_entity.deserialize_aws_json_1_1(item)
        )
    return out
