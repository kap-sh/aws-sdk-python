"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorSearchFilterNameEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "ACTION_CONNECTOR_NAME",
        "ACTION_CONNECTOR_TYPE",
        "QUICKSIGHT_OWNER",
        "QUICKSIGHT_VIEWER_OR_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    )
)


def serialize_json(value: ActionConnectorSearchFilterNameEnum) -> str:
    return value


def deserialize_json(data: str) -> ActionConnectorSearchFilterNameEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ActionConnectorSearchFilterNameEnum value: {data!r}"
        )
    return cast(ActionConnectorSearchFilterNameEnum, data)
