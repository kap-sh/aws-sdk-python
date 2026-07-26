"""Generated from Smithy shape ``com.amazonaws.launchwizard#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_pattern_version_filter

FilterList: TypeAlias = list[
    "capo_launch_wizard.types.deployment_pattern_version_filter.DeploymentPatternVersionFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterList) -> list:
    import capo_launch_wizard.types.deployment_pattern_version_filter

    out: list = []
    for item in value:
        out.append(
            capo_launch_wizard.types.deployment_pattern_version_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FilterList:
    import capo_launch_wizard.types.deployment_pattern_version_filter

    out: FilterList = []
    for item in data:
        out.append(
            capo_launch_wizard.types.deployment_pattern_version_filter.deserialize_json(
                item
            )
        )
    return out
