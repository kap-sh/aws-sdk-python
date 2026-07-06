"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectSyntaxRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.customer_input_string
    import aws_sdk_comprehend.types.syntax_language_code


class DetectSyntaxRequest(TypedDict, closed=True):
    text: "aws_sdk_comprehend.types.customer_input_string.CustomerInputString"
    """<p>A UTF-8 string. The maximum string size is 5 KB.</p>"""
    language_code: "aws_sdk_comprehend.types.syntax_language_code.SyntaxLanguageCode"
    r"""<p>The language code of the input documents. You can specify any of the following languages supported by Amazon Comprehend: German (\"de\"), English (\"en\"), Spanish (\"es\"), French (\"fr\"), Italian (\"it\"), or Portuguese (\"pt\").</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectSyntaxRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    import aws_sdk_comprehend.types.syntax_language_code

    out["LanguageCode"] = (
        aws_sdk_comprehend.types.syntax_language_code.serialize_aws_json_1_1(
            value["language_code"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectSyntaxRequest:
    out: DetectSyntaxRequest = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("DetectSyntaxRequest.text required")
    if "LanguageCode" in data:
        import aws_sdk_comprehend.types.syntax_language_code

        out["language_code"] = (
            aws_sdk_comprehend.types.syntax_language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("DetectSyntaxRequest.language_code required")
    return out
