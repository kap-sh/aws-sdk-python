"""Generated from Smithy shape ``com.amazonaws.transcribe#LanguageOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.language_code

LanguageOptions: TypeAlias = list["aws_sdk_transcribe.types.language_code.LanguageCode"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguageOptions) -> list:
    import aws_sdk_transcribe.types.language_code

    out: list = []
    for item in value:
        out.append(aws_sdk_transcribe.types.language_code.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LanguageOptions:
    import aws_sdk_transcribe.types.language_code

    out: LanguageOptions = []
    for item in data:
        out.append(
            aws_sdk_transcribe.types.language_code.deserialize_aws_json_1_1(item)
        )
    return out
