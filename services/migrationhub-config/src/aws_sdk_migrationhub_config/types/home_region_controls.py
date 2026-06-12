"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#HomeRegionControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhub_config.types.home_region_control

HomeRegionControls: TypeAlias = list[
    "aws_sdk_migrationhub_config.types.home_region_control.HomeRegionControl"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HomeRegionControls) -> list:
    import aws_sdk_migrationhub_config.types.home_region_control

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhub_config.types.home_region_control.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HomeRegionControls:
    import aws_sdk_migrationhub_config.types.home_region_control

    out: HomeRegionControls = []
    for item in data:
        out.append(
            aws_sdk_migrationhub_config.types.home_region_control.deserialize_aws_json_1_1(
                item
            )
        )
    return out
