"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorErrorType``."""

from typing import Literal, TypeAlias, cast

ActionConnectorErrorType: TypeAlias = Literal["INTERNAL_FAILURE",]


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnectorErrorType) -> str:
    return value


def deserialize_json(data: str) -> ActionConnectorErrorType:
    return cast(ActionConnectorErrorType, data)
