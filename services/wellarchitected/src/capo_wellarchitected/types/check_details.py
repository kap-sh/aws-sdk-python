"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.check_detail

CheckDetails: TypeAlias = list["capo_wellarchitected.types.check_detail.CheckDetail"]


# --- restJson1 ser/de ---
def serialize_json(value: CheckDetails) -> list:
    import capo_wellarchitected.types.check_detail

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.check_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> CheckDetails:
    import capo_wellarchitected.types.check_detail

    out: CheckDetails = []
    for item in data:
        out.append(capo_wellarchitected.types.check_detail.deserialize_json(item))
    return out
