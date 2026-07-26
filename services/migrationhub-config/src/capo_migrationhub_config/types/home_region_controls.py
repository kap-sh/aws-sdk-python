"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#HomeRegionControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhub_config.types.home_region_control

HomeRegionControls: TypeAlias = list[
    "capo_migrationhub_config.types.home_region_control.HomeRegionControl"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HomeRegionControls) -> list:
    import capo_migrationhub_config.types.home_region_control

    out: list = []
    for item in value:
        out.append(
            capo_migrationhub_config.types.home_region_control.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HomeRegionControls:
    import capo_migrationhub_config.types.home_region_control

    out: HomeRegionControls = []
    for item in data:
        out.append(
            capo_migrationhub_config.types.home_region_control.deserialize_aws_json_1_1(
                item
            )
        )
    return out
