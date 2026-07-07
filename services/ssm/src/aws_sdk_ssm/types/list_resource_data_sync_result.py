"""Generated from Smithy shape ``com.amazonaws.ssm#ListResourceDataSyncResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.resource_data_sync_item_list


class ListResourceDataSyncResult(TypedDict, closed=True):
    resource_data_sync_items: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_item_list.ResourceDataSyncItemList"
    ]
    """<p>A list of your current resource data sync configurations and their statuses.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceDataSyncResult) -> dict:
    out: dict = {}
    if "resource_data_sync_items" in value:
        import aws_sdk_ssm.types.resource_data_sync_item_list

        out["ResourceDataSyncItems"] = (
            aws_sdk_ssm.types.resource_data_sync_item_list.serialize_aws_json_1_1(
                value["resource_data_sync_items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceDataSyncResult:
    out: ListResourceDataSyncResult = {}  # type: ignore[typeddict-item]
    if "ResourceDataSyncItems" in data:
        import aws_sdk_ssm.types.resource_data_sync_item_list

        out["resource_data_sync_items"] = (
            aws_sdk_ssm.types.resource_data_sync_item_list.deserialize_aws_json_1_1(
                data["ResourceDataSyncItems"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
