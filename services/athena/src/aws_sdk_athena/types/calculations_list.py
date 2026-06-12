"""Generated from Smithy shape ``com.amazonaws.athena#CalculationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.calculation_summary

CalculationsList: TypeAlias = list[
    "aws_sdk_athena.types.calculation_summary.CalculationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalculationsList) -> list:
    import aws_sdk_athena.types.calculation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_athena.types.calculation_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CalculationsList:
    import aws_sdk_athena.types.calculation_summary

    out: CalculationsList = []
    for item in data:
        out.append(
            aws_sdk_athena.types.calculation_summary.deserialize_aws_json_1_1(item)
        )
    return out
