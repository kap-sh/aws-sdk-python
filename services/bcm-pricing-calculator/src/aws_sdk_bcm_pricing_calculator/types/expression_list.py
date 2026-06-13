"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ExpressionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.expression

ExpressionList: TypeAlias = list[
    "aws_sdk_bcm_pricing_calculator.types.expression.Expression"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExpressionList) -> list:
    import aws_sdk_bcm_pricing_calculator.types.expression

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.expression.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExpressionList:
    import aws_sdk_bcm_pricing_calculator.types.expression

    out: ExpressionList = []
    for item in data:
        out.append(
            aws_sdk_bcm_pricing_calculator.types.expression.deserialize_aws_json_1_0(
                item
            )
        )
    return out
