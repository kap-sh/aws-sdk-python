"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#FilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_recommended_actions.types.filter_value

FilterValues: TypeAlias = list[
    "capo_bcm_recommended_actions.types.filter_value.FilterValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> FilterValues:
    return list(data)
