"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEntityRecognizerSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entity_recognizer_summaries_list
    import aws_sdk_comprehend.types.string


class ListEntityRecognizerSummariesResponse(TypedDict, closed=True):
    entity_recognizer_summaries_list: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_summaries_list.EntityRecognizerSummariesList"
    ]
    """<p>The list entity recognizer summaries.</p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntityRecognizerSummariesResponse) -> dict:
    out: dict = {}
    if "entity_recognizer_summaries_list" in value:
        import aws_sdk_comprehend.types.entity_recognizer_summaries_list

        out["EntityRecognizerSummariesList"] = (
            aws_sdk_comprehend.types.entity_recognizer_summaries_list.serialize_aws_json_1_1(
                value["entity_recognizer_summaries_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntityRecognizerSummariesResponse:
    out: ListEntityRecognizerSummariesResponse = {}  # type: ignore[typeddict-item]
    if "EntityRecognizerSummariesList" in data:
        import aws_sdk_comprehend.types.entity_recognizer_summaries_list

        out["entity_recognizer_summaries_list"] = (
            aws_sdk_comprehend.types.entity_recognizer_summaries_list.deserialize_aws_json_1_1(
                data["EntityRecognizerSummariesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
