"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeImagePermissionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.name
    import aws_sdk_appstream.types.shared_image_permissions_list
    import aws_sdk_appstream.types.string


class DescribeImagePermissionsResult(TypedDict):
    name: NotRequired["aws_sdk_appstream.types.name.Name"]
    """<p>The name of the private image.</p>"""
    shared_image_permissions_list: NotRequired[
        "aws_sdk_appstream.types.shared_image_permissions_list.SharedImagePermissionsList"
    ]
    """<p>The permissions for a private image that you own. </p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImagePermissionsResult) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "shared_image_permissions_list" in value:
        import aws_sdk_appstream.types.shared_image_permissions_list

        out["SharedImagePermissionsList"] = (
            aws_sdk_appstream.types.shared_image_permissions_list.serialize_aws_json_1_1(
                value["shared_image_permissions_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImagePermissionsResult:
    out: DescribeImagePermissionsResult = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SharedImagePermissionsList" in data:
        import aws_sdk_appstream.types.shared_image_permissions_list

        out["shared_image_permissions_list"] = (
            aws_sdk_appstream.types.shared_image_permissions_list.deserialize_aws_json_1_1(
                data["SharedImagePermissionsList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
