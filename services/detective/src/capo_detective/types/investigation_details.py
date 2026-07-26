"""Generated from Smithy shape ``com.amazonaws.detective#InvestigationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.investigation_detail

InvestigationDetails: TypeAlias = list[
    "capo_detective.types.investigation_detail.InvestigationDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationDetails) -> list:
    import capo_detective.types.investigation_detail

    out: list = []
    for item in value:
        out.append(capo_detective.types.investigation_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> InvestigationDetails:
    import capo_detective.types.investigation_detail

    out: InvestigationDetails = []
    for item in data:
        out.append(capo_detective.types.investigation_detail.deserialize_json(item))
    return out
