"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfTextSegments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.text_segment

ListOfTextSegments: TypeAlias = list[
    "aws_sdk_comprehend.types.text_segment.TextSegment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfTextSegments) -> list:
    import aws_sdk_comprehend.types.text_segment

    out: list = []
    for item in value:
        out.append(aws_sdk_comprehend.types.text_segment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfTextSegments:
    import aws_sdk_comprehend.types.text_segment

    out: ListOfTextSegments = []
    for item in data:
        out.append(aws_sdk_comprehend.types.text_segment.deserialize_aws_json_1_1(item))
    return out
