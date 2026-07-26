"""Generated from Smithy shape ``com.amazonaws.athena#CalculationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.calculation_summary

CalculationsList: TypeAlias = list[
    "capo_athena.types.calculation_summary.CalculationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalculationsList) -> list:
    import capo_athena.types.calculation_summary

    out: list = []
    for item in value:
        out.append(capo_athena.types.calculation_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CalculationsList:
    import capo_athena.types.calculation_summary

    out: CalculationsList = []
    for item in data:
        out.append(capo_athena.types.calculation_summary.deserialize_aws_json_1_1(item))
    return out
