"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectDominantLanguageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.customer_input_string_list


class BatchDetectDominantLanguageRequest(TypedDict, closed=True):
    text_list: (
        "aws_sdk_comprehend.types.customer_input_string_list.CustomerInputStringList"
    )
    """<p>A list containing the UTF-8 encoded text of the input documents. The list can contain a maximum of 25 documents. Each document should contain at least 20 characters. The maximum size of each document is 5 KB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectDominantLanguageRequest) -> dict:
    out: dict = {}
    import aws_sdk_comprehend.types.customer_input_string_list

    out["TextList"] = (
        aws_sdk_comprehend.types.customer_input_string_list.serialize_aws_json_1_1(
            value["text_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectDominantLanguageRequest:
    out: BatchDetectDominantLanguageRequest = {}  # type: ignore[typeddict-item]
    if "TextList" in data:
        import aws_sdk_comprehend.types.customer_input_string_list

        out["text_list"] = (
            aws_sdk_comprehend.types.customer_input_string_list.deserialize_aws_json_1_1(
                data["TextList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDetectDominantLanguageRequest.text_list required"
        )
    return out
