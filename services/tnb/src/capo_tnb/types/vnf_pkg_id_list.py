"""Generated from Smithy shape ``com.amazonaws.tnb#VnfPkgIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_tnb.types.vnf_pkg_id

VnfPkgIdList: TypeAlias = list["capo_tnb.types.vnf_pkg_id.VnfPkgId"]


# --- restJson1 ser/de ---
def serialize_json(value: VnfPkgIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> VnfPkgIdList:
    return list(data)
