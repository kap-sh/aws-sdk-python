"""Generated from Smithy shape ``com.amazonaws.novaact#ModelIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.model_id

ModelIdList: TypeAlias = list["aws_sdk_nova_act.types.model_id.ModelId"]


# --- restJson1 ser/de ---
def serialize_json(value: ModelIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ModelIdList:
    return list(data)
