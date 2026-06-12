"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.icd10_cm_entity

ICD10CMEntityList: TypeAlias = list[
    "aws_sdk_comprehendmedical.types.icd10_cm_entity.ICD10CMEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMEntityList) -> list:
    import aws_sdk_comprehendmedical.types.icd10_cm_entity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehendmedical.types.icd10_cm_entity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ICD10CMEntityList:
    import aws_sdk_comprehendmedical.types.icd10_cm_entity

    out: ICD10CMEntityList = []
    for item in data:
        out.append(
            aws_sdk_comprehendmedical.types.icd10_cm_entity.deserialize_aws_json_1_1(
                item
            )
        )
    return out
