"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorSearchFilterNameEnum``."""

from typing import Literal, TypeAlias, cast

ActionConnectorSearchFilterNameEnum: TypeAlias = Literal[
    "ACTION_CONNECTOR_NAME",
    "ACTION_CONNECTOR_TYPE",
    "QUICKSIGHT_OWNER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnectorSearchFilterNameEnum) -> str:
    return value


def deserialize_json(data: str) -> ActionConnectorSearchFilterNameEnum:
    return cast(ActionConnectorSearchFilterNameEnum, data)
