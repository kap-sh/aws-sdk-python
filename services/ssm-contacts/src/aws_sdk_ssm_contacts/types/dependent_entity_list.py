"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DependentEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.dependent_entity

DependentEntityList: TypeAlias = list[
    "aws_sdk_ssm_contacts.types.dependent_entity.DependentEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependentEntityList) -> list:
    import aws_sdk_ssm_contacts.types.dependent_entity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_contacts.types.dependent_entity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DependentEntityList:
    import aws_sdk_ssm_contacts.types.dependent_entity

    out: DependentEntityList = []
    for item in data:
        out.append(
            aws_sdk_ssm_contacts.types.dependent_entity.deserialize_aws_json_1_1(item)
        )
    return out
