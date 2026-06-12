"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfDominantLanguages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.dominant_language

ListOfDominantLanguages: TypeAlias = list[
    "aws_sdk_comprehend.types.dominant_language.DominantLanguage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfDominantLanguages) -> list:
    import aws_sdk_comprehend.types.dominant_language

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.dominant_language.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfDominantLanguages:
    import aws_sdk_comprehend.types.dominant_language

    out: ListOfDominantLanguages = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.dominant_language.deserialize_aws_json_1_1(item)
        )
    return out
