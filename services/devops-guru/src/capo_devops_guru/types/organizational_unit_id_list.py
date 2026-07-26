"""Generated from Smithy shape ``com.amazonaws.devopsguru#OrganizationalUnitIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.organizational_unit_id

OrganizationalUnitIdList: TypeAlias = list[
    "capo_devops_guru.types.organizational_unit_id.OrganizationalUnitId"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalUnitIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> OrganizationalUnitIdList:
    return list(data)
