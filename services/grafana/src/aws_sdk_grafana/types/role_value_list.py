"""Generated from Smithy shape ``com.amazonaws.grafana#RoleValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_grafana.types.role_value

RoleValueList: TypeAlias = list["aws_sdk_grafana.types.role_value.RoleValue"]


# --- restJson1 ser/de ---
def serialize_json(value: RoleValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> RoleValueList:
    return list(data)
