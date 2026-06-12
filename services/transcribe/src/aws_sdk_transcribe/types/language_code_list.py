"""Generated from Smithy shape ``com.amazonaws.transcribe#LanguageCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.language_code_item

LanguageCodeList: TypeAlias = list[
    "aws_sdk_transcribe.types.language_code_item.LanguageCodeItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguageCodeList) -> list:
    import aws_sdk_transcribe.types.language_code_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe.types.language_code_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LanguageCodeList:
    import aws_sdk_transcribe.types.language_code_item

    out: LanguageCodeList = []
    for item in data:
        out.append(
            aws_sdk_transcribe.types.language_code_item.deserialize_aws_json_1_1(item)
        )
    return out
