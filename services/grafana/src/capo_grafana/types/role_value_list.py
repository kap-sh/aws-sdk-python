"""Generated from Smithy shape ``com.amazonaws.grafana#RoleValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_grafana.types.role_value

RoleValueList: TypeAlias = list["capo_grafana.types.role_value.RoleValue"]


# --- restJson1 ser/de ---
def serialize_json(value: RoleValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> RoleValueList:
    return list(data)
