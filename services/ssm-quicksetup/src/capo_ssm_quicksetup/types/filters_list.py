"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#FiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.filter

FiltersList: TypeAlias = list["capo_ssm_quicksetup.types.filter.Filter"]


# --- restJson1 ser/de ---
def serialize_json(value: FiltersList) -> list:
    import capo_ssm_quicksetup.types.filter

    out: list = []
    for item in value:
        out.append(capo_ssm_quicksetup.types.filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> FiltersList:
    import capo_ssm_quicksetup.types.filter

    out: FiltersList = []
    for item in data:
        out.append(capo_ssm_quicksetup.types.filter.deserialize_json(item))
    return out
