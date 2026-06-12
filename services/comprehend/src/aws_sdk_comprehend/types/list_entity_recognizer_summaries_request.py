"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEntityRecognizerSummariesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.max_results_integer
    import aws_sdk_comprehend.types.string


class ListEntityRecognizerSummariesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""
    max_results: NotRequired[
        "aws_sdk_comprehend.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>The maximum number of results to return on each page. The default is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntityRecognizerSummariesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntityRecognizerSummariesRequest:
    out: ListEntityRecognizerSummariesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
