"""Generated from Smithy shape ``com.amazonaws.tnb#GetSolVnfcResourceInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_tnb.types.get_sol_vnfc_resource_info

GetSolVnfcResourceInfoList: TypeAlias = list[
    "capo_tnb.types.get_sol_vnfc_resource_info.GetSolVnfcResourceInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetSolVnfcResourceInfoList) -> list:
    import capo_tnb.types.get_sol_vnfc_resource_info

    out: list = []
    for item in value:
        out.append(capo_tnb.types.get_sol_vnfc_resource_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> GetSolVnfcResourceInfoList:
    import capo_tnb.types.get_sol_vnfc_resource_info

    out: GetSolVnfcResourceInfoList = []
    for item in data:
        out.append(capo_tnb.types.get_sol_vnfc_resource_info.deserialize_json(item))
    return out
