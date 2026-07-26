"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorSuppliedValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.connector_supplied_value

ConnectorSuppliedValueList: TypeAlias = list[
    "capo_appflow.types.connector_supplied_value.ConnectorSuppliedValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorSuppliedValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConnectorSuppliedValueList:
    return list(data)
