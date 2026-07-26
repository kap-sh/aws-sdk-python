"""Generated from Smithy shape ``com.amazonaws.kendra#AssociateEntitiesToExperienceFailedEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.failed_entity

AssociateEntitiesToExperienceFailedEntityList: TypeAlias = list[
    "capo_kendra.types.failed_entity.FailedEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AssociateEntitiesToExperienceFailedEntityList,
) -> list:
    import capo_kendra.types.failed_entity

    out: list = []
    for item in value:
        out.append(capo_kendra.types.failed_entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> AssociateEntitiesToExperienceFailedEntityList:
    import capo_kendra.types.failed_entity

    out: AssociateEntitiesToExperienceFailedEntityList = []
    for item in data:
        out.append(capo_kendra.types.failed_entity.deserialize_aws_json_1_1(item))
    return out
