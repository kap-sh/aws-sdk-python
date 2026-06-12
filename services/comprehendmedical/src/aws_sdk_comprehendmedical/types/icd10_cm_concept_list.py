"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMConceptList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.icd10_cm_concept

ICD10CMConceptList: TypeAlias = list[
    "aws_sdk_comprehendmedical.types.icd10_cm_concept.ICD10CMConcept"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMConceptList) -> list:
    import aws_sdk_comprehendmedical.types.icd10_cm_concept

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehendmedical.types.icd10_cm_concept.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ICD10CMConceptList:
    import aws_sdk_comprehendmedical.types.icd10_cm_concept

    out: ICD10CMConceptList = []
    for item in data:
        out.append(
            aws_sdk_comprehendmedical.types.icd10_cm_concept.deserialize_aws_json_1_1(
                item
            )
        )
    return out
