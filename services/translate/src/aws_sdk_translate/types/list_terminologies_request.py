"""Generated from Smithy shape ``com.amazonaws.translate#ListTerminologiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_translate.types.max_results_integer
    import aws_sdk_translate.types.next_token


class ListTerminologiesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_translate.types.next_token.NextToken"]
    """<p>If the result of the request to ListTerminologies was truncated, include the NextToken to fetch the next group of custom terminologies. </p>"""
    max_results: NotRequired[
        "aws_sdk_translate.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>The maximum number of custom terminologies returned per list request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTerminologiesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTerminologiesRequest:
    out: ListTerminologiesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
