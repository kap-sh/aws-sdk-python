"""Generated from Smithy shape ``com.amazonaws.qbusiness#RelevantContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.relevant_content

RelevantContentList: TypeAlias = list[
    "aws_sdk_qbusiness.types.relevant_content.RelevantContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: RelevantContentList) -> list:
    import aws_sdk_qbusiness.types.relevant_content

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.relevant_content.serialize_json(item))
    return out


def deserialize_json(data: list) -> RelevantContentList:
    import aws_sdk_qbusiness.types.relevant_content

    out: RelevantContentList = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.relevant_content.deserialize_json(item))
    return out
