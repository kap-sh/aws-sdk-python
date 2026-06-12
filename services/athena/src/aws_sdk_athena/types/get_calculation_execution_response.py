"""Generated from Smithy shape ``com.amazonaws.athena#GetCalculationExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.calculation_execution_id
    import aws_sdk_athena.types.calculation_result
    import aws_sdk_athena.types.calculation_statistics
    import aws_sdk_athena.types.calculation_status
    import aws_sdk_athena.types.description_string
    import aws_sdk_athena.types.s3_uri
    import aws_sdk_athena.types.session_id


class GetCalculationExecutionResponse(TypedDict):
    calculation_execution_id: NotRequired[
        "aws_sdk_athena.types.calculation_execution_id.CalculationExecutionId"
    ]
    """<p>The calculation execution UUID.</p>"""
    session_id: NotRequired["aws_sdk_athena.types.session_id.SessionId"]
    """<p>The session ID that the calculation ran in.</p>"""
    description: NotRequired[
        "aws_sdk_athena.types.description_string.DescriptionString"
    ]
    """<p>The description of the calculation execution.</p>"""
    working_directory: NotRequired["aws_sdk_athena.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 location in which calculation results are stored.</p>"""
    status: NotRequired["aws_sdk_athena.types.calculation_status.CalculationStatus"]
    """<p>Contains information about the status of the calculation.</p>"""
    statistics: NotRequired[
        "aws_sdk_athena.types.calculation_statistics.CalculationStatistics"
    ]
    """<p>Contains information about the data processing unit (DPU) execution time and progress. This field is populated only when statistics are available.</p>"""
    result: NotRequired["aws_sdk_athena.types.calculation_result.CalculationResult"]
    """<p>Contains result information. This field is populated only if the calculation is completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCalculationExecutionResponse) -> dict:
    out: dict = {}
    if "calculation_execution_id" in value:
        out["CalculationExecutionId"] = value["calculation_execution_id"]
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
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
    if "result" in value:
        import aws_sdk_athena.types.calculation_result

        out["Result"] = aws_sdk_athena.types.calculation_result.serialize_aws_json_1_1(
            value["result"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCalculationExecutionResponse:
    out: GetCalculationExecutionResponse = {}  # type: ignore[typeddict-item]
    if "CalculationExecutionId" in data:
        out["calculation_execution_id"] = data["CalculationExecutionId"]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "WorkingDirectory" in data:
        out["working_directory"] = data["WorkingDirectory"]
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
    if "Result" in data:
        import aws_sdk_athena.types.calculation_result

        out["result"] = (
            aws_sdk_athena.types.calculation_result.deserialize_aws_json_1_1(
                data["Result"]
            )
        )
    return out
