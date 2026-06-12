"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeApplicationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.arn_list
    import aws_sdk_appstream.types.integer
    import aws_sdk_appstream.types.string


class DescribeApplicationsRequest(TypedDict):
    arns: NotRequired["aws_sdk_appstream.types.arn_list.ArnList"]
    """<p>The ARNs for the applications.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""
    max_results: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationsRequest) -> dict:
    out: dict = {}
    if "arns" in value:
        import aws_sdk_appstream.types.arn_list

        out["Arns"] = aws_sdk_appstream.types.arn_list.serialize_aws_json_1_1(
            value["arns"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationsRequest:
    out: DescribeApplicationsRequest = {}  # type: ignore[typeddict-item]
    if "Arns" in data:
        import aws_sdk_appstream.types.arn_list

        out["arns"] = aws_sdk_appstream.types.arn_list.deserialize_aws_json_1_1(
            data["Arns"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
