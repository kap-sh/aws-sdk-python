"""Generated from Smithy shape ``com.amazonaws.comprehend#ContainsPiiEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.language_code
    import capo_comprehend.types.string


class ContainsPiiEntitiesRequest(TypedDict, closed=True):
    text: "capo_comprehend.types.string.String"
    """<p>A UTF-8 text string. The maximum string size is 100 KB.</p>"""
    language_code: "capo_comprehend.types.language_code.LanguageCode"
    """<p>The language of the input documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainsPiiEntitiesRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    import capo_comprehend.types.language_code

    out["LanguageCode"] = capo_comprehend.types.language_code.serialize_aws_json_1_1(
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
        import capo_comprehend.types.language_code

        out["language_code"] = (
            capo_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError("ContainsPiiEntitiesRequest.language_code required")
    return out
