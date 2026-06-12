"""Generated from Smithy shape ``com.amazonaws.comprehend#ContainsPiiEntitiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.language_code
    import aws_sdk_comprehend.types.string


class ContainsPiiEntitiesRequest(TypedDict):
    text: "aws_sdk_comprehend.types.string.String"
    """<p>A UTF-8 text string. The maximum string size is 100 KB.</p>"""
    language_code: "aws_sdk_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainsPiiEntitiesRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    import aws_sdk_comprehend.types.language_code

    out["LanguageCode"] = aws_sdk_comprehend.types.language_code.serialize_aws_json_1_1(
        value["language_code"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainsPiiEntitiesRequest:
    out: ContainsPiiEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("ContainsPiiEntitiesRequest.text required")
    if "LanguageCode" in data:
        import aws_sdk_comprehend.types.language_code

        out["language_code"] = (
            aws_sdk_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("ContainsPiiEntitiesRequest.language_code required")
    return out
