"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorModeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.connector_mode

ConnectorModeList: TypeAlias = list["capo_appflow.types.connector_mode.ConnectorMode"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorModeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConnectorModeList:
    return list(data)
