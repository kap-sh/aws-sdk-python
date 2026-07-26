"""Generated from Smithy shape ``com.amazonaws.athena#CalculationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.calculation_execution_id
    import capo_athena.types.calculation_status
    import capo_athena.types.description_string


class CalculationSummary(TypedDict, closed=True):
    calculation_execution_id: NotRequired[
        "capo_athena.types.calculation_execution_id.CalculationExecutionId"
    ]
    """<p>The calculation execution UUID.</p>"""
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>A description of the calculation.</p>"""
    status: NotRequired["capo_athena.types.calculation_status.CalculationStatus"]
    """<p>Contains information about the status of the calculation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalculationSummary) -> dict:
    out: dict = {}
    if "calculation_execution_id" in value:
        out["CalculationExecutionId"] = value["calculation_execution_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_athena.types.calculation_status

        out["Status"] = capo_athena.types.calculation_status.serialize_aws_json_1_1(
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
        import capo_athena.types.calculation_status

        out["status"] = capo_athena.types.calculation_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
