"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProfileNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.connector_profile_name

ConnectorProfileNameList: TypeAlias = list[
    "capo_appflow.types.connector_profile_name.ConnectorProfileName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProfileNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConnectorProfileNameList:
    return list(data)
