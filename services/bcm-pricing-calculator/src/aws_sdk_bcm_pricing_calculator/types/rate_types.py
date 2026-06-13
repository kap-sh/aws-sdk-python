"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#RateTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.rate_type

RateTypes: TypeAlias = list["aws_sdk_bcm_pricing_calculator.types.rate_type.RateType"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RateTypes) -> list:
    import aws_sdk_bcm_pricing_calculator.types.rate_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.rate_type.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RateTypes:
    import aws_sdk_bcm_pricing_calculator.types.rate_type

    out: RateTypes = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.rate_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out
