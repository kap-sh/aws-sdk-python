"""Generated from Smithy shape ``com.amazonaws.comprehend#BatchDetectDominantLanguageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.batch_item_error_list
    import aws_sdk_comprehend.types.list_of_detect_dominant_language_result


class BatchDetectDominantLanguageResponse(TypedDict):
    result_list: "aws_sdk_comprehend.types.list_of_detect_dominant_language_result.ListOfDetectDominantLanguageResult"
    """<p>A list of objects containing the results of the operation. The results are sorted in ascending order by the <code>Index</code> field and match the order of the documents in the input list. If all of the documents contain an error, the <code>ResultList</code> is empty.</p>"""
    error_list: "aws_sdk_comprehend.types.batch_item_error_list.BatchItemErrorList"
    """<p>A list containing one object for each document that contained an error. The results are sorted in ascending order by the <code>Index</code> field and match the order of the documents in the input list. If there are no errors in the batch, the <code>ErrorList</code> is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDetectDominantLanguageResponse) -> dict:
    out: dict = {}
    import aws_sdk_comprehend.types.list_of_detect_dominant_language_result

    out["ResultList"] = (
        aws_sdk_comprehend.types.list_of_detect_dominant_language_result.serialize_aws_json_1_1(
            value["result_list"]
        )
    )
    import aws_sdk_comprehend.types.batch_item_error_list

    out["ErrorList"] = (
        aws_sdk_comprehend.types.batch_item_error_list.serialize_aws_json_1_1(
            value["error_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDetectDominantLanguageResponse:
    out: BatchDetectDominantLanguageResponse = {}  # type: ignore[typeddict-item]
    if "ResultList" in data:
        import aws_sdk_comprehend.types.list_of_detect_dominant_language_result

        out["result_list"] = (
            aws_sdk_comprehend.types.list_of_detect_dominant_language_result.deserialize_aws_json_1_1(
                data["ResultList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDetectDominantLanguageResponse.result_list required"
        )
    if "ErrorList" in data:
        import aws_sdk_comprehend.types.batch_item_error_list

        out["error_list"] = (
            aws_sdk_comprehend.types.batch_item_error_list.deserialize_aws_json_1_1(
                data["ErrorList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDetectDominantLanguageResponse.error_list required"
        )
    return out
