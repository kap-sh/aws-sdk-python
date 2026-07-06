"""Generated from Smithy shape ``com.amazonaws.transcribe#LanguageCodeItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.duration_in_seconds
    import aws_sdk_transcribe.types.language_code


class LanguageCodeItem(TypedDict, closed=True):
    language_code: NotRequired["aws_sdk_transcribe.types.language_code.LanguageCode"]
    """<p>Provides the language code for each language identified in your media.</p>"""
    duration_in_seconds: NotRequired[
        "aws_sdk_transcribe.types.duration_in_seconds.DurationInSeconds"
    ]
    """<p>Provides the total time, in seconds, each identified language is spoken in your media.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LanguageCodeItem) -> dict:
    out: dict = {}
    if "language_code" in value:
        import aws_sdk_transcribe.types.language_code

        out["LanguageCode"] = (
            aws_sdk_transcribe.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LanguageCodeItem:
    out: LanguageCodeItem = {}  # type: ignore[typeddict-item]
    if "LanguageCode" in data:
        import aws_sdk_transcribe.types.language_code

        out["language_code"] = (
            aws_sdk_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    return out
