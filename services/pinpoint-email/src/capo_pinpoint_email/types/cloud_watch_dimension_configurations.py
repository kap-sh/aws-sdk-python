"""Generated from Smithy shape ``com.amazonaws.pinpointemail#CloudWatchDimensionConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.cloud_watch_dimension_configuration

CloudWatchDimensionConfigurations: TypeAlias = list[
    "capo_pinpoint_email.types.cloud_watch_dimension_configuration.CloudWatchDimensionConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchDimensionConfigurations) -> list:
    import capo_pinpoint_email.types.cloud_watch_dimension_configuration

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_email.types.cloud_watch_dimension_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CloudWatchDimensionConfigurations:
    import capo_pinpoint_email.types.cloud_watch_dimension_configuration

    out: CloudWatchDimensionConfigurations = []
    for item in data:
        out.append(
            capo_pinpoint_email.types.cloud_watch_dimension_configuration.deserialize_json(
                item
            )
        )
    return out
