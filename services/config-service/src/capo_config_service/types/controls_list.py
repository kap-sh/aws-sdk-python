"""Generated from Smithy shape ``com.amazonaws.configservice#ControlsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.string_with_char_limit128

ControlsList: TypeAlias = list[
    "capo_config_service.types.string_with_char_limit128.StringWithCharLimit128"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ControlsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ControlsList:
    return list(data)
