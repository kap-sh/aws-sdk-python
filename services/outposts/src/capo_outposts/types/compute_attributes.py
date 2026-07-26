"""Generated from Smithy shape ``com.amazonaws.outposts#ComputeAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.asset_instance_capacity_list
    import capo_outposts.types.compute_asset_state
    import capo_outposts.types.host_id
    import capo_outposts.types.instance_families
    import capo_outposts.types.vcpu_count


class ComputeAttributes(TypedDict, closed=True):
    host_id: NotRequired["capo_outposts.types.host_id.HostId"]
    """<p> The host ID of the Dedicated Host on the asset. </p>"""
    state: NotRequired["capo_outposts.types.compute_asset_state.ComputeAssetState"]
    """<p>The state.</p> <ul> <li> <p>ACTIVE - The asset is available and can provide capacity for new compute resources.</p> </li> <li> <p>ISOLATED - The asset is undergoing maintenance and can't provide capacity for new compute resources. Existing compute resources on the asset are not affected.</p> </li> <li> <p>RETIRING - The underlying hardware for the asset is degraded. Capacity for new compute resources is reduced. Amazon Web Services sends notifications for resources that must be stopped before the asset can be replaced.</p> </li> <li> <p>INSTALLING - The asset is being installed and can't yet provide capacity for new compute resources.</p> </li> </ul>"""
    instance_families: NotRequired[
        "capo_outposts.types.instance_families.InstanceFamilies"
    ]
    """<p>A list of the names of instance families that are currently associated with a given asset.</p>"""
    instance_type_capacities: NotRequired[
        "capo_outposts.types.asset_instance_capacity_list.AssetInstanceCapacityList"
    ]
    """<p>The instance type capacities configured for this asset. This can be changed through a capacity task.</p>"""
    max_vcpus: NotRequired["capo_outposts.types.vcpu_count.VCPUCount"]
    """<p>The maximum number of vCPUs possible for the specified asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeAttributes) -> dict:
    out: dict = {}
    if "host_id" in value:
        out["HostId"] = value["host_id"]
    if "state" in value:
        import capo_outposts.types.compute_asset_state

        out["State"] = capo_outposts.types.compute_asset_state.serialize_json(
            value["state"]
        )
    if "instance_families" in value:
        import capo_outposts.types.instance_families

        out["InstanceFamilies"] = capo_outposts.types.instance_families.serialize_json(
            value["instance_families"]
        )
    if "instance_type_capacities" in value:
        import capo_outposts.types.asset_instance_capacity_list

        out["InstanceTypeCapacities"] = (
            capo_outposts.types.asset_instance_capacity_list.serialize_json(
                value["instance_type_capacities"]
            )
        )
    if "max_vcpus" in value:
        out["MaxVcpus"] = value["max_vcpus"]
    return out


def deserialize_json(data: dict) -> ComputeAttributes:
    out: ComputeAttributes = {}  # type: ignore[typeddict-item]
    if "HostId" in data:
        out["host_id"] = data["HostId"]
    if "State" in data:
        import capo_outposts.types.compute_asset_state

        out["state"] = capo_outposts.types.compute_asset_state.deserialize_json(
            data["State"]
        )
    if "InstanceFamilies" in data:
        import capo_outposts.types.instance_families

        out["instance_families"] = (
            capo_outposts.types.instance_families.deserialize_json(
                data["InstanceFamilies"]
            )
        )
    if "InstanceTypeCapacities" in data:
        import capo_outposts.types.asset_instance_capacity_list

        out["instance_type_capacities"] = (
            capo_outposts.types.asset_instance_capacity_list.deserialize_json(
                data["InstanceTypeCapacities"]
            )
        )
    if "MaxVcpus" in data:
        out["max_vcpus"] = data["MaxVcpus"]
    return out
