"""Generated from Smithy shape ``com.amazonaws.costexplorer#PlatformDifferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.platform_difference

PlatformDifferences: TypeAlias = list[
    "capo_cost_explorer.types.platform_difference.PlatformDifference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlatformDifferences) -> list:
    import capo_cost_explorer.types.platform_difference

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.platform_difference.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PlatformDifferences:
    import capo_cost_explorer.types.platform_difference

    out: PlatformDifferences = []
    for item in data:
        out.append(
            capo_cost_explorer.types.platform_difference.deserialize_aws_json_1_1(item)
        )
    return out
