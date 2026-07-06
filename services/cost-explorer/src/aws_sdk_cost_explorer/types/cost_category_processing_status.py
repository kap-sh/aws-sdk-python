"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryProcessingStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_status
    import aws_sdk_cost_explorer.types.cost_category_status_component


class CostCategoryProcessingStatus(TypedDict, closed=True):
    component: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_status_component.CostCategoryStatusComponent"
    ]
    """<p>The Cost Management product name of the applied status. </p>"""
    status: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_status.CostCategoryStatus"
    ]
    """<p>The process status for a specific cost category. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryProcessingStatus) -> dict:
    out: dict = {}
    if "component" in value:
        import aws_sdk_cost_explorer.types.cost_category_status_component

        out["Component"] = (
            aws_sdk_cost_explorer.types.cost_category_status_component.serialize_aws_json_1_1(
                value["component"]
            )
        )
    if "status" in value:
        import aws_sdk_cost_explorer.types.cost_category_status

        out["Status"] = (
            aws_sdk_cost_explorer.types.cost_category_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategoryProcessingStatus:
    out: CostCategoryProcessingStatus = {}  # type: ignore[typeddict-item]
    if "Component" in data:
        import aws_sdk_cost_explorer.types.cost_category_status_component

        out["component"] = (
            aws_sdk_cost_explorer.types.cost_category_status_component.deserialize_aws_json_1_1(
                data["Component"]
            )
        )
    if "Status" in data:
        import aws_sdk_cost_explorer.types.cost_category_status

        out["status"] = (
            aws_sdk_cost_explorer.types.cost_category_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
