"""Generated from Smithy shape ``com.amazonaws.grafana#VpceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_grafana.types.vpce_id

VpceIds: TypeAlias = list["aws_sdk_grafana.types.vpce_id.VpceId"]


# --- restJson1 ser/de ---
def serialize_json(value: VpceIds) -> list:
    return list(value)


def deserialize_json(data: list) -> VpceIds:
    return list(data)
