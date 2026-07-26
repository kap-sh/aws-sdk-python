"""Generated from Smithy shape ``com.amazonaws.workdocs#OrganizationUserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.user

OrganizationUserList: TypeAlias = list["capo_workdocs.types.user.User"]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationUserList) -> list:
    import capo_workdocs.types.user

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.user.serialize_json(item))
    return out


def deserialize_json(data: list) -> OrganizationUserList:
    import capo_workdocs.types.user

    out: OrganizationUserList = []
    for item in data:
        out.append(capo_workdocs.types.user.deserialize_json(item))
    return out
