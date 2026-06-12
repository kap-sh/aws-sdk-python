"""Generated from Smithy shape ``com.amazonaws.transcribe#VocabularyFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.vocabulary_filter_info

VocabularyFilters: TypeAlias = list[
    "aws_sdk_transcribe.types.vocabulary_filter_info.VocabularyFilterInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VocabularyFilters) -> list:
    import aws_sdk_transcribe.types.vocabulary_filter_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe.types.vocabulary_filter_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VocabularyFilters:
    import aws_sdk_transcribe.types.vocabulary_filter_info

    out: VocabularyFilters = []
    for item in data:
        out.append(
            aws_sdk_transcribe.types.vocabulary_filter_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
