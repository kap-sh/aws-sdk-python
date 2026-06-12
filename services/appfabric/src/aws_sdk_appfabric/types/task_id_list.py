"""Generated from Smithy shape ``com.amazonaws.appfabric#TaskIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.uuid

TaskIdList: TypeAlias = list["aws_sdk_appfabric.types.uuid.UUID"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> TaskIdList:
    return list(data)
