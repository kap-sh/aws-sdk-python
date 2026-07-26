"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListResourceInventoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.resource_inventory_list
    import capo_license_manager.types.string


class ListResourceInventoryResponse(TypedDict, closed=True):
    resource_inventory_list: NotRequired[
        "capo_license_manager.types.resource_inventory_list.ResourceInventoryList"
    ]
    """<p>Information about the resources.</p>"""
    next_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceInventoryResponse) -> dict:
    out: dict = {}
    if "resource_inventory_list" in value:
        import capo_license_manager.types.resource_inventory_list

        out["ResourceInventoryList"] = (
            capo_license_manager.types.resource_inventory_list.serialize_aws_json_1_1(
                value["resource_inventory_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceInventoryResponse:
    out: ListResourceInventoryResponse = {}  # type: ignore[typeddict-item]
    if "ResourceInventoryList" in data:
        import capo_license_manager.types.resource_inventory_list

        out["resource_inventory_list"] = (
            capo_license_manager.types.resource_inventory_list.deserialize_aws_json_1_1(
                data["ResourceInventoryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
