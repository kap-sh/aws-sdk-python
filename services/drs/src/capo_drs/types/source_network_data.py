"""Generated from Smithy shape ``com.amazonaws.drs#SourceNetworkData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.large_bounded_string
    import capo_drs.types.source_network_id
    import capo_drs.types.vpc_id


class SourceNetworkData(TypedDict, closed=True):
    source_network_id: NotRequired["capo_drs.types.source_network_id.SourceNetworkID"]
    """<p>Source Network ID.</p>"""
    source_vpc: NotRequired["capo_drs.types.vpc_id.VpcID"]
    """<p>VPC ID protected by the Source Network.</p>"""
    target_vpc: NotRequired["capo_drs.types.vpc_id.VpcID"]
    """<p>ID of the recovered VPC following Source Network recovery.</p>"""
    stack_name: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>CloudFormation stack name that was deployed for recovering the Source Network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceNetworkData) -> dict:
    out: dict = {}
    if "source_network_id" in value:
        out["sourceNetworkID"] = value["source_network_id"]
    if "source_vpc" in value:
        out["sourceVpc"] = value["source_vpc"]
    if "target_vpc" in value:
        out["targetVpc"] = value["target_vpc"]
    if "stack_name" in value:
        out["stackName"] = value["stack_name"]
    return out


def deserialize_json(data: dict) -> SourceNetworkData:
    out: SourceNetworkData = {}  # type: ignore[typeddict-item]
    if "sourceNetworkID" in data:
        out["source_network_id"] = data["sourceNetworkID"]
    if "sourceVpc" in data:
        out["source_vpc"] = data["sourceVpc"]
    if "targetVpc" in data:
        out["target_vpc"] = data["targetVpc"]
    if "stackName" in data:
        out["stack_name"] = data["stackName"]
    return out
