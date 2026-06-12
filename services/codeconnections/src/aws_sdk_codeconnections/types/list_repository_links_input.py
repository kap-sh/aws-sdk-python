"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListRepositoryLinksInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.max_results
    import aws_sdk_codeconnections.types.sharp_next_token


class ListRepositoryLinksInput(TypedDict):
    max_results: "aws_sdk_codeconnections.types.max_results.MaxResults"
    """<p> A non-zero, non-negative integer used to limit the number of returned results.</p>"""
    next_token: NotRequired[
        "aws_sdk_codeconnections.types.sharp_next_token.SharpNextToken"
    ]
    """<p> An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRepositoryLinksInput) -> dict:
    out: dict = {}
    out["MaxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRepositoryLinksInput:
    out: ListRepositoryLinksInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
