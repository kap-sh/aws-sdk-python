"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListInsightsOrganizationalUnitIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.organizational_unit_id

ListInsightsOrganizationalUnitIdList: TypeAlias = list[
    "capo_devops_guru.types.organizational_unit_id.OrganizationalUnitId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsOrganizationalUnitIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ListInsightsOrganizationalUnitIdList:
    return list(data)
