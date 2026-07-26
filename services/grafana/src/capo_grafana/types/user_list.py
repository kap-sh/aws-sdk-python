"""Generated from Smithy shape ``com.amazonaws.grafana#UserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_grafana.types.user

UserList: TypeAlias = list["capo_grafana.types.user.User"]


# --- restJson1 ser/de ---
def serialize_json(value: UserList) -> list:
    import capo_grafana.types.user

    out: list = []
    for item in value:
        out.append(capo_grafana.types.user.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserList:
    import capo_grafana.types.user

    out: UserList = []
    for item in data:
        out.append(capo_grafana.types.user.deserialize_json(item))
    return out
