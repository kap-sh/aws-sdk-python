"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GetResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.pagination_token
    import aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping_list


class GetResourcesOutput(TypedDict, closed=True):
    pagination_token: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.pagination_token.PaginationToken"
    ]
    """<p>A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the <code>PaginationToken</code> value in the request for the next page.</p>"""
    resource_tag_mapping_list: NotRequired[
        "aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping_list.ResourceTagMappingList"
    ]
    """<p>A list of resource ARNs and the tags (keys and values) associated with each.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcesOutput) -> dict:
    out: dict = {}
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "resource_tag_mapping_list" in value:
        import aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping_list

        out["ResourceTagMappingList"] = (
            aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping_list.serialize_aws_json_1_1(
                value["resource_tag_mapping_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcesOutput:
    out: GetResourcesOutput = {}  # type: ignore[typeddict-item]
    if "PaginationToken" in data:
        out["pagination_token"] = data["PaginationToken"]
    if "ResourceTagMappingList" in data:
        import aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping_list

        out["resource_tag_mapping_list"] = (
            aws_sdk_resource_groups_tagging_api.types.resource_tag_mapping_list.deserialize_aws_json_1_1(
                data["ResourceTagMappingList"]
            )
        )
    return out
