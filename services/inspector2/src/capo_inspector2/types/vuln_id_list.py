"""Generated from Smithy shape ``com.amazonaws.inspector2#VulnIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.vuln_id

VulnIdList: TypeAlias = list["capo_inspector2.types.vuln_id.VulnId"]


# --- restJson1 ser/de ---
def serialize_json(value: VulnIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> VulnIdList:
    return list(data)
