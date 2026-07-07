"""Generated from Smithy shape ``com.amazonaws.emr#DescribeReleaseLabelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.max_results_number
    import aws_sdk_emr.types.string


class DescribeReleaseLabelInput(TypedDict, closed=True):
    release_label: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The target release label to be described.</p>"""
    next_token: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>The pagination token. Reserved for future use. Currently set to null.</p>"""
    max_results: NotRequired["aws_sdk_emr.types.max_results_number.MaxResultsNumber"]
    """<p>Reserved for future use. Currently set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReleaseLabelInput) -> dict:
    out: dict = {}
    if "release_label" in value:
        out["ReleaseLabel"] = value["release_label"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReleaseLabelInput:
    out: DescribeReleaseLabelInput = {}  # type: ignore[typeddict-item]
    if "ReleaseLabel" in data:
        out["release_label"] = data["ReleaseLabel"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
