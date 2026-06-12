"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ConfigurationSetNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.configuration_set_name

ConfigurationSetNameList: TypeAlias = list[
    "aws_sdk_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationSetNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConfigurationSetNameList:
    return list(data)
