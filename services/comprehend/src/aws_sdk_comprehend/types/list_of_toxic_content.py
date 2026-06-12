"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfToxicContent``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.toxic_content

ListOfToxicContent: TypeAlias = list[
    "aws_sdk_comprehend.types.toxic_content.ToxicContent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfToxicContent) -> list:
    import aws_sdk_comprehend.types.toxic_content

    out: list = []
    for item in value:
        out.append(aws_sdk_comprehend.types.toxic_content.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfToxicContent:
    import aws_sdk_comprehend.types.toxic_content

    out: ListOfToxicContent = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.toxic_content.deserialize_aws_json_1_1(item)
        )
    return out
