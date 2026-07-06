"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectPiiEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.language_code
    import aws_sdk_comprehend.types.string


class DetectPiiEntitiesRequest(TypedDict, closed=True):
    text: "aws_sdk_comprehend.types.string.String"
    """<p>A UTF-8 text string. The maximum string size is 100 KB.</p>"""
    language_code: "aws_sdk_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input text. Enter the language code for English (en) or Spanish (es).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectPiiEntitiesRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    import aws_sdk_comprehend.types.language_code

    out["LanguageCode"] = aws_sdk_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectPiiEntitiesRequest:
    out: DetectPiiEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("DetectPiiEntitiesRequest.text required")
    if "LanguageCode" in data:
        import aws_sdk_comprehend.types.language_code

        out["language_code"] = (
            aws_sdk_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("DetectPiiEntitiesRequest.language_code required")
    return out
