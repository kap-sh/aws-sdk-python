"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeActivationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.describe_activations_filter_list
    import aws_sdk_ssm.types.max_results
    import aws_sdk_ssm.types.next_token


class DescribeActivationsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_ssm.types.describe_activations_filter_list.DescribeActivationsFilterList"
    ]
    """<p>A filter to view information about your activations.</p>"""
    max_results: NotRequired["aws_sdk_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeActivationsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_ssm.types.describe_activations_filter_list

        out["Filters"] = (
            aws_sdk_ssm.types.describe_activations_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeActivationsRequest:
    out: DescribeActivationsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_ssm.types.describe_activations_filter_list

        out["filters"] = (
            aws_sdk_ssm.types.describe_activations_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
