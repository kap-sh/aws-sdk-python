"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeTagsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.resource_tag_list


class DescribeTagsResponse(TypedDict):
    resource_tags: NotRequired[
        "aws_sdk_direct_connect.types.resource_tag_list.ResourceTagList"
    ]
    """<p>Information about the tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsResponse) -> dict:
    out: dict = {}
    if "resource_tags" in value:
        import aws_sdk_direct_connect.types.resource_tag_list

        out["resourceTags"] = (
            aws_sdk_direct_connect.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsResponse:
    out: DescribeTagsResponse = {}  # type: ignore[typeddict-item]
    if "resourceTags" in data:
        import aws_sdk_direct_connect.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_direct_connect.types.resource_tag_list.deserialize_aws_json_1_1(
                data["resourceTags"]
            )
        )
    return out
