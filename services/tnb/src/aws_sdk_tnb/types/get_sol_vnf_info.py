"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolVnfInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_tnb.types.get_sol_vnfc_resource_info_list
    import aws_sdk_tnb.types.vnf_operational_state


class GetSolVnfInfo(TypedDict):
    vnf_state: NotRequired[
        "aws_sdk_tnb.types.vnf_operational_state.VnfOperationalState"
    ]
    """<p>State of the network function instance.</p>"""
    vnfc_resource_info: NotRequired[
        "aws_sdk_tnb.types.get_sol_vnfc_resource_info_list.GetSolVnfcResourceInfoList"
    ]
    """<p>Compute info used by the network function instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSolVnfInfo) -> dict:
    out: dict = {}
    if "vnf_state" in value:
        import aws_sdk_tnb.types.vnf_operational_state

        out["vnfState"] = aws_sdk_tnb.types.vnf_operational_state.serialize_json(
            value["vnf_state"]
        )
    if "vnfc_resource_info" in value:
        import aws_sdk_tnb.types.get_sol_vnfc_resource_info_list

        out["vnfcResourceInfo"] = (
            aws_sdk_tnb.types.get_sol_vnfc_resource_info_list.serialize_json(
                value["vnfc_resource_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSolVnfInfo:
    out: GetSolVnfInfo = {}  # type: ignore[typeddict-item]
    if "vnfState" in data:
        import aws_sdk_tnb.types.vnf_operational_state

        out["vnf_state"] = aws_sdk_tnb.types.vnf_operational_state.deserialize_json(
            data["vnfState"]
        )
    if "vnfcResourceInfo" in data:
        import aws_sdk_tnb.types.get_sol_vnfc_resource_info_list

        out["vnfc_resource_info"] = (
            aws_sdk_tnb.types.get_sol_vnfc_resource_info_list.deserialize_json(
                data["vnfcResourceInfo"]
            )
        )
    return out
