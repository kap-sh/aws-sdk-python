"""Generated from Smithy shape ``com.amazonaws.sesv2#CloudWatchDimensionConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.cloud_watch_dimension_configuration

CloudWatchDimensionConfigurations: TypeAlias = list[
    "aws_sdk_sesv2.types.cloud_watch_dimension_configuration.CloudWatchDimensionConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchDimensionConfigurations) -> list:
    import aws_sdk_sesv2.types.cloud_watch_dimension_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sesv2.types.cloud_watch_dimension_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CloudWatchDimensionConfigurations:
    import aws_sdk_sesv2.types.cloud_watch_dimension_configuration

    out: CloudWatchDimensionConfigurations = []
    for item in data:
        out.append(
            aws_sdk_sesv2.types.cloud_watch_dimension_configuration.deserialize_json(
                item
            )
        )
    return out
