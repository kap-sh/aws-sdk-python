"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeRegionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.next_token
    import aws_sdk_directory_service.types.regions_description


class DescribeRegionsResult(TypedDict):
    regions_description: NotRequired[
        "aws_sdk_directory_service.types.regions_description.RegionsDescription"
    ]
    """<p>List of Region information related to the directory for each replicated Region.</p>"""
    next_token: NotRequired["aws_sdk_directory_service.types.next_token.NextToken"]
    """<p>If not null, more results are available. Pass this value for the <code>NextToken</code> parameter in a subsequent call to <a>DescribeRegions</a> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRegionsResult) -> dict:
    out: dict = {}
    if "regions_description" in value:
        import aws_sdk_directory_service.types.regions_description

        out["RegionsDescription"] = (
            aws_sdk_directory_service.types.regions_description.serialize_aws_json_1_1(
                value["regions_description"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRegionsResult:
    out: DescribeRegionsResult = {}  # type: ignore[typeddict-item]
    if "RegionsDescription" in data:
        import aws_sdk_directory_service.types.regions_description

        out["regions_description"] = (
            aws_sdk_directory_service.types.regions_description.deserialize_aws_json_1_1(
                data["RegionsDescription"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
