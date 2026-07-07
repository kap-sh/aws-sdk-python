"""Generated from Smithy shape ``com.amazonaws.rekognition#ListStreamProcessorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.max_results
    import aws_sdk_rekognition.types.pagination_token


class ListStreamProcessorsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_rekognition.types.pagination_token.PaginationToken"
    ]
    """<p>If the previous response was incomplete (because there are more stream processors to retrieve), Amazon Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of stream processors. </p>"""
    max_results: NotRequired["aws_sdk_rekognition.types.max_results.MaxResults"]
    """<p>Maximum number of stream processors you want Amazon Rekognition Video to return in the response. The default is 1000. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStreamProcessorsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStreamProcessorsRequest:
    out: ListStreamProcessorsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
