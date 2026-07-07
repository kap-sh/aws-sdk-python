"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEntityRecognizersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entity_recognizer_filter
    import aws_sdk_comprehend.types.max_results_integer
    import aws_sdk_comprehend.types.string


class ListEntityRecognizersRequest(TypedDict, closed=True):
    filter: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_filter.EntityRecognizerFilter"
    ]
    """<p>Filters the list of entities returned. You can filter on <code>Status</code>, <code>SubmitTimeBefore</code>, or <code>SubmitTimeAfter</code>. You can only set one filter at a time.</p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""
    max_results: NotRequired[
        "aws_sdk_comprehend.types.max_results_integer.MaxResultsInteger"
    ]
    """<p> The maximum number of results to return on each page. The default is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntityRecognizersRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_comprehend.types.entity_recognizer_filter

        out["Filter"] = (
            aws_sdk_comprehend.types.entity_recognizer_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntityRecognizersRequest:
    out: ListEntityRecognizersRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import aws_sdk_comprehend.types.entity_recognizer_filter

        out["filter"] = (
            aws_sdk_comprehend.types.entity_recognizer_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
