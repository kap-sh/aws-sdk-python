"""Generated from Smithy shape ``com.amazonaws.costexplorer#ESInstanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_boolean
    import capo_cost_explorer.types.generic_string


class ESInstanceDetails(TypedDict, closed=True):
    instance_class: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The class of instance that Amazon Web Services recommends.</p>"""
    instance_size: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The size of instance that Amazon Web Services recommends.</p>"""
    region: NotRequired["capo_cost_explorer.types.generic_string.GenericString"]
    """<p>The Amazon Web Services Region of the recommended reservation.</p>"""
    current_generation: "capo_cost_explorer.types.generic_boolean.GenericBoolean"
    """<p>Determines whether the recommendation is for a current-generation instance.</p>"""
    size_flex_eligible: "capo_cost_explorer.types.generic_boolean.GenericBoolean"
    """<p>Determines whether the recommended reservation is size flexible.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ESInstanceDetails) -> dict:
    out: dict = {}
    if "instance_class" in value:
        out["InstanceClass"] = value["instance_class"]
    if "instance_size" in value:
        out["InstanceSize"] = value["instance_size"]
    if "region" in value:
        out["Region"] = value["region"]
    out["CurrentGeneration"] = value.get("current_generation", False)
    out["SizeFlexEligible"] = value.get("size_flex_eligible", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ESInstanceDetails:
    out: ESInstanceDetails = {}  # type: ignore[typeddict-item]
    if "InstanceClass" in data:
        out["instance_class"] = data["InstanceClass"]
    if "InstanceSize" in data:
        out["instance_size"] = data["InstanceSize"]
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
