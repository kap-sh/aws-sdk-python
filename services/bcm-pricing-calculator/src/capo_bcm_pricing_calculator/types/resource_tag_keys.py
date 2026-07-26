"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ResourceTagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.resource_tag_key

ResourceTagKeys: TypeAlias = list[
    "capo_bcm_pricing_calculator.types.resource_tag_key.ResourceTagKey"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTagKeys) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ResourceTagKeys:
    return list(data)
