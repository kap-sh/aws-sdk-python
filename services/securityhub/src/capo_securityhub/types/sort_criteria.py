"""Generated from Smithy shape ``com.amazonaws.securityhub#SortCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.sort_criterion

SortCriteria: TypeAlias = list["capo_securityhub.types.sort_criterion.SortCriterion"]


# --- restJson1 ser/de ---
def serialize_json(value: SortCriteria) -> list:
    import capo_securityhub.types.sort_criterion

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.sort_criterion.serialize_json(item))
    return out


def deserialize_json(data: list) -> SortCriteria:
    import capo_securityhub.types.sort_criterion

    out: SortCriteria = []
    for item in data:
        out.append(capo_securityhub.types.sort_criterion.deserialize_json(item))
    return out
