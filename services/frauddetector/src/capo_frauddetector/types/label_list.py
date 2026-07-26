"""Generated from Smithy shape ``com.amazonaws.frauddetector#labelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.label

labelList: TypeAlias = list["capo_frauddetector.types.label.Label"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: labelList) -> list:
    import capo_frauddetector.types.label

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.label.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> labelList:
    import capo_frauddetector.types.label

    out: labelList = []
    for item in data:
        out.append(capo_frauddetector.types.label.deserialize_aws_json_1_1(item))
    return out
