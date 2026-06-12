"""Generated from Smithy shape ``com.amazonaws.kendra#AssociateEntitiesToExperienceFailedEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.failed_entity

AssociateEntitiesToExperienceFailedEntityList: TypeAlias = list[
    "aws_sdk_kendra.types.failed_entity.FailedEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AssociateEntitiesToExperienceFailedEntityList,
) -> list:
    import aws_sdk_kendra.types.failed_entity

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.failed_entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> AssociateEntitiesToExperienceFailedEntityList:
    import aws_sdk_kendra.types.failed_entity

    out: AssociateEntitiesToExperienceFailedEntityList = []
    for item in data:
        out.append(aws_sdk_kendra.types.failed_entity.deserialize_aws_json_1_1(item))
    return out
