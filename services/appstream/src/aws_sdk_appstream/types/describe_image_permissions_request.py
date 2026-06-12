"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeImagePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.aws_account_id_list
    import aws_sdk_appstream.types.max_results
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.string


class DescribeImagePermissionsRequest(TypedDict):
    name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the private image for which to describe permissions. The image must be one that you own. </p>"""
    max_results: NotRequired["aws_sdk_appstream.types.max_results.MaxResults"]
    """<p>The maximum size of each page of results.</p>"""
    shared_aws_account_ids: NotRequired[
        "aws_sdk_appstream.types.aws_account_id_list.AwsAccountIdList"
    ]
    """<p>The 12-digit identifier of one or more AWS accounts with which the image is shared.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImagePermissionsRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "shared_aws_account_ids" in value:
        import aws_sdk_appstream.types.aws_account_id_list

        out["SharedAwsAccountIds"] = (
            aws_sdk_appstream.types.aws_account_id_list.serialize_aws_json_1_1(
                value["shared_aws_account_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImagePermissionsRequest:
    out: DescribeImagePermissionsRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "SharedAwsAccountIds" in data:
        import aws_sdk_appstream.types.aws_account_id_list

        out["shared_aws_account_ids"] = (
            aws_sdk_appstream.types.aws_account_id_list.deserialize_aws_json_1_1(
                data["SharedAwsAccountIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
