"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeResourceGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.failed_items
    import aws_sdk_inspector.types.resource_group_list


class DescribeResourceGroupsResponse(TypedDict):
    resource_groups: "aws_sdk_inspector.types.resource_group_list.ResourceGroupList"
    """<p>Information about a resource group.</p>"""
    failed_items: "aws_sdk_inspector.types.failed_items.FailedItems"
    """<p>Resource group details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourceGroupsResponse) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.resource_group_list

    out["resourceGroups"] = (
        aws_sdk_inspector.types.resource_group_list.serialize_aws_json_1_1(
            value["resource_groups"]
        )
    )
    import aws_sdk_inspector.types.failed_items

    out["failedItems"] = aws_sdk_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourceGroupsResponse:
    out: DescribeResourceGroupsResponse = {}  # type: ignore[typeddict-item]
    if "resourceGroups" in data:
        import aws_sdk_inspector.types.resource_group_list

        out["resource_groups"] = (
            aws_sdk_inspector.types.resource_group_list.deserialize_aws_json_1_1(
                data["resourceGroups"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeResourceGroupsResponse.resource_groups required"
        )
    if "failedItems" in data:
        import aws_sdk_inspector.types.failed_items

        out["failed_items"] = (
            aws_sdk_inspector.types.failed_items.deserialize_aws_json_1_1(
                data["failedItems"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeResourceGroupsResponse.failed_items required"
        )
    return out
