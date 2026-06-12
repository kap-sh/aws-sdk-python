"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectSentimentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.customer_input_string
    import aws_sdk_comprehend.types.language_code


class DetectSentimentRequest(TypedDict):
    text: "aws_sdk_comprehend.types.customer_input_string.CustomerInputString"
    """<p>A UTF-8 text string. The maximum string size is 5 KB.</p>"""
    language_code: "aws_sdk_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input documents. You can specify any of the primary languages supported by Amazon Comprehend. All documents must be in the same language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectSentimentRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    import aws_sdk_comprehend.types.language_code

    out["LanguageCode"] = aws_sdk_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectSentimentRequest:
    out: DetectSentimentRequest = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("DetectSentimentRequest.text required")
    if "LanguageCode" in data:
        import aws_sdk_comprehend.types.language_code

        out["language_code"] = (
            aws_sdk_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("DetectSentimentRequest.language_code required")
    return out
