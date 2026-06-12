"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfToxicLabels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.toxic_labels

ListOfToxicLabels: TypeAlias = list["aws_sdk_comprehend.types.toxic_labels.ToxicLabels"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfToxicLabels) -> list:
    import aws_sdk_comprehend.types.toxic_labels

    out: list = []
    for item in value:
        out.append(aws_sdk_comprehend.types.toxic_labels.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfToxicLabels:
    import aws_sdk_comprehend.types.toxic_labels

    out: ListOfToxicLabels = []
    for item in data:
        out.append(aws_sdk_comprehend.types.toxic_labels.deserialize_aws_json_1_1(item))
    return out
