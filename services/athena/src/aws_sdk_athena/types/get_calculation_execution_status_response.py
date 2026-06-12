"""Generated from Smithy shape ``com.amazonaws.athena#GetCalculationExecutionStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.calculation_statistics
    import aws_sdk_athena.types.calculation_status


class GetCalculationExecutionStatusResponse(TypedDict):
    status: NotRequired["aws_sdk_athena.types.calculation_status.CalculationStatus"]
    """<p>Contains information about the calculation execution status.</p>"""
    statistics: NotRequired[
        "aws_sdk_athena.types.calculation_statistics.CalculationStatistics"
    ]
    """<p>Contains information about the DPU execution time and progress.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCalculationExecutionStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_athena.types.calculation_status

        out["Status"] = aws_sdk_athena.types.calculation_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "statistics" in value:
        import aws_sdk_athena.types.calculation_statistics

        out["Statistics"] = (
            aws_sdk_athena.types.calculation_statistics.serialize_aws_json_1_1(
                value["statistics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCalculationExecutionStatusResponse:
    out: GetCalculationExecutionStatusResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_athena.types.calculation_status

        out["status"] = (
            aws_sdk_athena.types.calculation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Statistics" in data:
        import aws_sdk_athena.types.calculation_statistics

        out["statistics"] = (
            aws_sdk_athena.types.calculation_statistics.deserialize_aws_json_1_1(
                data["Statistics"]
            )
        )
    return out
