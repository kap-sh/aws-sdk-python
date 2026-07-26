"""Generated from Smithy shape ``com.amazonaws.detective#MembershipDatasourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.membership_datasources

MembershipDatasourcesList: TypeAlias = list[
    "capo_detective.types.membership_datasources.MembershipDatasources"
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipDatasourcesList) -> list:
    import capo_detective.types.membership_datasources

    out: list = []
    for item in value:
        out.append(capo_detective.types.membership_datasources.serialize_json(item))
    return out


def deserialize_json(data: list) -> MembershipDatasourcesList:
    import capo_detective.types.membership_datasources

    out: MembershipDatasourcesList = []
    for item in data:
        out.append(capo_detective.types.membership_datasources.deserialize_json(item))
    return out
