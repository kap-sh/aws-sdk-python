"""Generated from Smithy shape ``com.amazonaws.athena#ClassificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.classification

ClassificationList: TypeAlias = list["capo_athena.types.classification.Classification"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClassificationList) -> list:
    import capo_athena.types.classification

    out: list = []
    for item in value:
        out.append(capo_athena.types.classification.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClassificationList:
    import capo_athena.types.classification

    out: ClassificationList = []
    for item in data:
        out.append(capo_athena.types.classification.deserialize_aws_json_1_1(item))
    return out
