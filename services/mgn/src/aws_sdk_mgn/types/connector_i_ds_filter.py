"""Generated from Smithy shape ``com.amazonaws.mgn#ConnectorIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.connector_id

ConnectorIDsFilter: TypeAlias = list["aws_sdk_mgn.types.connector_id.ConnectorID"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> ConnectorIDsFilter:
    return list(data)
