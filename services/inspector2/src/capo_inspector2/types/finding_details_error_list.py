"""Generated from Smithy shape ``com.amazonaws.inspector2#FindingDetailsErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.finding_details_error

FindingDetailsErrorList: TypeAlias = list[
    "capo_inspector2.types.finding_details_error.FindingDetailsError"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingDetailsErrorList) -> list:
    import capo_inspector2.types.finding_details_error

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.finding_details_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingDetailsErrorList:
    import capo_inspector2.types.finding_details_error

    out: FindingDetailsErrorList = []
    for item in data:
        out.append(capo_inspector2.types.finding_details_error.deserialize_json(item))
    return out
