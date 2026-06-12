"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMTraitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.icd10_cm_trait

ICD10CMTraitList: TypeAlias = list[
    "aws_sdk_comprehendmedical.types.icd10_cm_trait.ICD10CMTrait"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMTraitList) -> list:
    import aws_sdk_comprehendmedical.types.icd10_cm_trait

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehendmedical.types.icd10_cm_trait.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ICD10CMTraitList:
    import aws_sdk_comprehendmedical.types.icd10_cm_trait

    out: ICD10CMTraitList = []
    for item in data:
        out.append(
            aws_sdk_comprehendmedical.types.icd10_cm_trait.deserialize_aws_json_1_1(
                item
            )
        )
    return out
