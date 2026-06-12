"""Generated from Smithy shape ``com.amazonaws.athena#CalculationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.calculation_execution_id
    import aws_sdk_athena.types.calculation_status
    import aws_sdk_athena.types.description_string


class CalculationSummary(TypedDict):
    calculation_execution_id: NotRequired[
        "aws_sdk_athena.types.calculation_execution_id.CalculationExecutionId"
    ]
    """<p>The calculation execution UUID.</p>"""
    description: NotRequired[
        "aws_sdk_athena.types.description_string.DescriptionString"
    ]
    """<p>A description of the calculation.</p>"""
    status: NotRequired["aws_sdk_athena.types.calculation_status.CalculationStatus"]
    """<p>Contains information about the status of the calculation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalculationSummary) -> dict:
    out: dict = {}
    if "calculation_execution_id" in value:
        out["CalculationExecutionId"] = value["calculation_execution_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_athena.types.calculation_status

        out["Status"] = aws_sdk_athena.types.calculation_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CalculationSummary:
    out: CalculationSummary = {}  # type: ignore[typeddict-item]
    if "CalculationExecutionId" in data:
        out["calculation_execution_id"] = data["CalculationExecutionId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_athena.types.calculation_status

        out["status"] = (
            aws_sdk_athena.types.calculation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    return out
