"""Generated from Smithy shape ``com.amazonaws.kendra#FailedEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.failed_entity

FailedEntityList: TypeAlias = list["capo_kendra.types.failed_entity.FailedEntity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedEntityList) -> list:
    import capo_kendra.types.failed_entity

    out: list = []
    for item in value:
        out.append(capo_kendra.types.failed_entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FailedEntityList:
    import capo_kendra.types.failed_entity

    out: FailedEntityList = []
    for item in data:
        out.append(capo_kendra.types.failed_entity.deserialize_aws_json_1_1(item))
    return out
