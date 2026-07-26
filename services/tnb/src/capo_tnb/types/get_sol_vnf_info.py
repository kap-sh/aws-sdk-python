"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolVnfInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_tnb.types.get_sol_vnfc_resource_info_list
    import capo_tnb.types.vnf_operational_state


class GetSolVnfInfo(TypedDict, closed=True):
    vnf_state: NotRequired["capo_tnb.types.vnf_operational_state.VnfOperationalState"]
    """<p>State of the network function instance.</p>"""
    vnfc_resource_info: NotRequired[
        "capo_tnb.types.get_sol_vnfc_resource_info_list.GetSolVnfcResourceInfoList"
    ]
    """<p>Compute info used by the network function instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolVnfInfo) -> dict:
    out: dict = {}
    if "vnf_state" in value:
        import capo_tnb.types.vnf_operational_state

        out["vnfState"] = capo_tnb.types.vnf_operational_state.serialize_json(
            value["vnf_state"]
        )
    if "vnfc_resource_info" in value:
        import capo_tnb.types.get_sol_vnfc_resource_info_list

        out["vnfcResourceInfo"] = (
            capo_tnb.types.get_sol_vnfc_resource_info_list.serialize_json(
                value["vnfc_resource_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSolVnfInfo:
    out: GetSolVnfInfo = {}  # type: ignore[typeddict-item]
    if "vnfState" in data:
        import capo_tnb.types.vnf_operational_state

        out["vnf_state"] = capo_tnb.types.vnf_operational_state.deserialize_json(
            data["vnfState"]
        )
    if "vnfcResourceInfo" in data:
        import capo_tnb.types.get_sol_vnfc_resource_info_list

        out["vnfc_resource_info"] = (
            capo_tnb.types.get_sol_vnfc_resource_info_list.deserialize_json(
                data["vnfcResourceInfo"]
            )
        )
    return out
