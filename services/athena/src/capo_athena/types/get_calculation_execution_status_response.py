"""Generated from Smithy shape ``com.amazonaws.athena#GetCalculationExecutionStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.calculation_statistics
    import capo_athena.types.calculation_status


class GetCalculationExecutionStatusResponse(TypedDict, closed=True):
    status: NotRequired["capo_athena.types.calculation_status.CalculationStatus"]
    """<p>Contains information about the calculation execution status.</p>"""
    statistics: NotRequired[
        "capo_athena.types.calculation_statistics.CalculationStatistics"
    ]
    """<p>Contains information about the DPU execution time and progress.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCalculationExecutionStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_athena.types.calculation_status

        out["Status"] = capo_athena.types.calculation_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "statistics" in value:
        import capo_athena.types.calculation_statistics

        out["Statistics"] = (
            capo_athena.types.calculation_statistics.serialize_aws_json_1_1(
                value["statistics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCalculationExecutionStatusResponse:
    out: GetCalculationExecutionStatusResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_athena.types.calculation_status

        out["status"] = capo_athena.types.calculation_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Statistics" in data:
        import capo_athena.types.calculation_statistics

        out["statistics"] = (
            capo_athena.types.calculation_statistics.deserialize_aws_json_1_1(
                data["Statistics"]
            )
        )
    return out
