"""Generated from Smithy shape ``com.amazonaws.ssmsap#ComponentIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.component_id

ComponentIdList: TypeAlias = list["aws_sdk_ssm_sap.types.component_id.ComponentId"]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ComponentIdList:
    return list(data)
