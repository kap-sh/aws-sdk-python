"""Generated from Smithy shape ``com.amazonaws.securityhub#PropagatingVgwSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.propagating_vgw_set_details

PropagatingVgwSetList: TypeAlias = list[
    "capo_securityhub.types.propagating_vgw_set_details.PropagatingVgwSetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: PropagatingVgwSetList) -> list:
    import capo_securityhub.types.propagating_vgw_set_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.propagating_vgw_set_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PropagatingVgwSetList:
    import capo_securityhub.types.propagating_vgw_set_details

    out: PropagatingVgwSetList = []
    for item in data:
        out.append(
            capo_securityhub.types.propagating_vgw_set_details.deserialize_json(item)
        )
    return out
