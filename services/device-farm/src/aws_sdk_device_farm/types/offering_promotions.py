"""Generated from Smithy shape ``com.amazonaws.devicefarm#OfferingPromotions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.offering_promotion

OfferingPromotions: TypeAlias = list[
    "aws_sdk_device_farm.types.offering_promotion.OfferingPromotion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OfferingPromotions) -> list:
    import aws_sdk_device_farm.types.offering_promotion

    out: list = []
    for item in value:
        out.append(
            aws_sdk_device_farm.types.offering_promotion.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OfferingPromotions:
    import aws_sdk_device_farm.types.offering_promotion

    out: OfferingPromotions = []
    for item in data:
        out.append(
            aws_sdk_device_farm.types.offering_promotion.deserialize_aws_json_1_1(item)
        )
    return out
