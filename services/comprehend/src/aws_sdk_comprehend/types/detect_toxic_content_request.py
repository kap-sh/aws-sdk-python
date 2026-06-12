"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectToxicContentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.language_code
    import aws_sdk_comprehend.types.list_of_text_segments


class DetectToxicContentRequest(TypedDict):
    text_segments: "aws_sdk_comprehend.types.list_of_text_segments.ListOfTextSegments"
    """<p>A list of up to 10 text strings. Each string has a maximum size of 1 KB, and the maximum size of the list is 10 KB.</p>"""
    language_code: "aws_sdk_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input text. Currently, English is the only supported language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectToxicContentRequest) -> dict:
    out: dict = {}
    import aws_sdk_comprehend.types.list_of_text_segments

    out["TextSegments"] = (
        aws_sdk_comprehend.types.list_of_text_segments.serialize_aws_json_1_1(
            value["text_segments"]
        )
    )
    import aws_sdk_comprehend.types.language_code

    out["LanguageCode"] = aws_sdk_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectToxicContentRequest:
    out: DetectToxicContentRequest = {}  # type: ignore[typeddict-item]
    if "TextSegments" in data:
        import aws_sdk_comprehend.types.list_of_text_segments

        out["text_segments"] = (
            aws_sdk_comprehend.types.list_of_text_segments.deserialize_aws_json_1_1(
                data["TextSegments"]
            )
        )
    else:
        raise DeserializationError("DetectToxicContentRequest.text_segments required")
    if "LanguageCode" in data:
        import aws_sdk_comprehend.types.language_code

        out["language_code"] = (
            aws_sdk_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("DetectToxicContentRequest.language_code required")
    return out
