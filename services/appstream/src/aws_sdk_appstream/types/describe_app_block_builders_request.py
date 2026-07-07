"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeAppBlockBuildersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.integer
    import aws_sdk_appstream.types.string
    import aws_sdk_appstream.types.string_list


class DescribeAppBlockBuildersRequest(TypedDict, closed=True):
    names: NotRequired["aws_sdk_appstream.types.string_list.StringList"]
    """<p>The names of the app block builders.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""
    max_results: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The maximum size of each page of results. The maximum value is 25.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppBlockBuildersRequest) -> dict:
    out: dict = {}
    if "names" in value:
        import aws_sdk_appstream.types.string_list

        out["Names"] = aws_sdk_appstream.types.string_list.serialize_aws_json_1_1(
            value["names"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAppBlockBuildersRequest:
    out: DescribeAppBlockBuildersRequest = {}  # type: ignore[typeddict-item]
    if "Names" in data:
        import aws_sdk_appstream.types.string_list

        out["names"] = aws_sdk_appstream.types.string_list.deserialize_aws_json_1_1(
            data["Names"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
