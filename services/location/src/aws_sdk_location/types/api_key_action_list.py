"""Generated from Smithy shape ``com.amazonaws.location#ApiKeyActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.api_key_action

ApiKeyActionList: TypeAlias = list["aws_sdk_location.types.api_key_action.ApiKeyAction"]


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyActionList) -> list:
    return list(value)


def deserialize_json(data: list) -> ApiKeyActionList:
    return list(data)
