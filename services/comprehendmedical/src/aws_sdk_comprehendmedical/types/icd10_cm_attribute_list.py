"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.icd10_cm_attribute

ICD10CMAttributeList: TypeAlias = list[
    "aws_sdk_comprehendmedical.types.icd10_cm_attribute.ICD10CMAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ICD10CMAttributeList) -> list:
    import aws_sdk_comprehendmedical.types.icd10_cm_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehendmedical.types.icd10_cm_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ICD10CMAttributeList:
    import aws_sdk_comprehendmedical.types.icd10_cm_attribute

    out: ICD10CMAttributeList = []
    for item in data:
        out.append(
            aws_sdk_comprehendmedical.types.icd10_cm_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out
