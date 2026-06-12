"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfClasses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_class

ListOfClasses: TypeAlias = list["aws_sdk_comprehend.types.document_class.DocumentClass"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfClasses) -> list:
    import aws_sdk_comprehend.types.document_class

    out: list = []
    for item in value:
        out.append(aws_sdk_comprehend.types.document_class.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfClasses:
    import aws_sdk_comprehend.types.document_class

    out: ListOfClasses = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.document_class.deserialize_aws_json_1_1(item)
        )
    return out
