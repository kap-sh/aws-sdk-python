"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInventoryDeletionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_deletions_list
    import aws_sdk_ssm.types.next_token


class DescribeInventoryDeletionsResult(TypedDict):
    inventory_deletions: NotRequired[
        "aws_sdk_ssm.types.inventory_deletions_list.InventoryDeletionsList"
    ]
    """<p>A list of status items for deleted inventory.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInventoryDeletionsResult) -> dict:
    out: dict = {}
    if "inventory_deletions" in value:
        import aws_sdk_ssm.types.inventory_deletions_list

        out["InventoryDeletions"] = (
            aws_sdk_ssm.types.inventory_deletions_list.serialize_aws_json_1_1(
                value["inventory_deletions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInventoryDeletionsResult:
    out: DescribeInventoryDeletionsResult = {}  # type: ignore[typeddict-item]
    if "InventoryDeletions" in data:
        import aws_sdk_ssm.types.inventory_deletions_list

        out["inventory_deletions"] = (
            aws_sdk_ssm.types.inventory_deletions_list.deserialize_aws_json_1_1(
                data["InventoryDeletions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
