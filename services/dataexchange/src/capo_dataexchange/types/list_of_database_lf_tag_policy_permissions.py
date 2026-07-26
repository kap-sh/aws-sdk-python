"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfDatabaseLFTagPolicyPermissions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.database_lf_tag_policy_permission

ListOfDatabaseLFTagPolicyPermissions: TypeAlias = list[
    "capo_dataexchange.types.database_lf_tag_policy_permission.DatabaseLFTagPolicyPermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDatabaseLFTagPolicyPermissions) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOfDatabaseLFTagPolicyPermissions:
    return list(data)
