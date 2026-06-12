"""Generated from Smithy shape ``com.amazonaws.opensearch#AppConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.app_config

AppConfigs: TypeAlias = list["aws_sdk_opensearch.types.app_config.AppConfig"]


# --- restJson1 ser/de ---
def serialize_json(value: AppConfigs) -> list:
    import aws_sdk_opensearch.types.app_config

    out: list = []
    for item in value:
        out.append(aws_sdk_opensearch.types.app_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppConfigs:
    import aws_sdk_opensearch.types.app_config

    out: AppConfigs = []
    for item in data:
        out.append(aws_sdk_opensearch.types.app_config.deserialize_json(item))
    return out
