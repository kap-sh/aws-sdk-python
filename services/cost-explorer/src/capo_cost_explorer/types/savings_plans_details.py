"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string


class SavingsPlansDetails(TypedDict, closed=True):
    region: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>A collection of Amazon Web Services resources in a geographic area. Each Amazon Web Services Region is isolated and independent of the other Regions.</p>"""
    instance_family: NotRequired[
        "capo_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>A group of instance types that Savings Plans applies to.</p>"""
    offering_id: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The unique ID that's used to distinguish Savings Plans from one another.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansDetails) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "instance_family" in value:
        out["InstanceFamily"] = value["instance_family"]
    if "offering_id" in value:
        out["OfferingId"] = value["offering_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansDetails:
    out: SavingsPlansDetails = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    if "InstanceFamily" in data:
        out["instance_family"] = data["InstanceFamily"]
    if "OfferingId" in data:
        out["offering_id"] = data["OfferingId"]
    return out
