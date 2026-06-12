"""Generated from Smithy shape ``com.amazonaws.glue#ClassifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.classifier

ClassifierList: TypeAlias = list["aws_sdk_glue.types.classifier.Classifier"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClassifierList) -> list:
    import aws_sdk_glue.types.classifier

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.classifier.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClassifierList:
    import aws_sdk_glue.types.classifier

    out: ClassifierList = []
    for item in data:
        out.append(aws_sdk_glue.types.classifier.deserialize_aws_json_1_1(item))
    return out
