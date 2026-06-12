"""Generated from Smithy shape ``com.amazonaws.appconfig#InvalidConfigurationDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.invalid_configuration_detail

InvalidConfigurationDetailList: TypeAlias = list[
    "aws_sdk_appconfig.types.invalid_configuration_detail.InvalidConfigurationDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidConfigurationDetailList) -> list:
    import aws_sdk_appconfig.types.invalid_configuration_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appconfig.types.invalid_configuration_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InvalidConfigurationDetailList:
    import aws_sdk_appconfig.types.invalid_configuration_detail

    out: InvalidConfigurationDetailList = []
    for item in data:
        out.append(
            aws_sdk_appconfig.types.invalid_configuration_detail.deserialize_json(item)
        )
    return out
