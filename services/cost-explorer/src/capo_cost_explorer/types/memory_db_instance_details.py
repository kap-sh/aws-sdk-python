"""Generated from Smithy shape ``com.amazonaws.costexplorer#MemoryDBInstanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_boolean
    import capo_cost_explorer.types.generic_string


class MemoryDBInstanceDetails(TypedDict, closed=True):
    family: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The instance family of the recommended reservation.</p>"""
    node_type: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The node type of the recommended reservation.</p>"""
    region: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The Amazon Web Services Region of the recommended reservation.</p>"""
    current_generation: "capo_cost_explorer.types.generic_boolean.GenericBoolean"
    """<p>Determines whether the recommendation is for a current generation instance.</p>"""
    size_flex_eligible: "capo_cost_explorer.types.generic_boolean.GenericBoolean"
    """<p>Determines whether the recommended reservation is size flexible.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemoryDBInstanceDetails) -> dict:
    out: dict = {}
    if "family" in value:
        out["Family"] = value["family"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "region" in value:
        out["Region"] = value["region"]
    out["CurrentGeneration"] = value.get("current_generation", False)
    out["SizeFlexEligible"] = value.get("size_flex_eligible", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> MemoryDBInstanceDetails:
    out: MemoryDBInstanceDetails = {}  # type: ignore[typeddict-item]
    if "Family" in data:
        out["family"] = data["Family"]
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "CurrentGeneration" in data:
        out["current_generation"] = data["CurrentGeneration"]
    else:
        out["current_generation"] = False
    if "SizeFlexEligible" in data:
        out["size_flex_eligible"] = data["SizeFlexEligible"]
    else:
        out["size_flex_eligible"] = False
    return out
