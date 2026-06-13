"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#GetExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.execution_status
    import aws_sdk_bcm_data_exports.types.export
    import aws_sdk_bcm_data_exports.types.generic_string


class GetExecutionResponse(TypedDict):
    execution_id: NotRequired[
        "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    ]
    """<p>The ID for this specific execution.</p>"""
    export: NotRequired["aws_sdk_bcm_data_exports.types.export.Export"]
    """<p>The export data for this specific execution. This export data is a snapshot from when the execution was generated. The data could be different from the current export data if the export was updated since the execution was generated.</p>"""
    execution_status: NotRequired[
        "aws_sdk_bcm_data_exports.types.execution_status.ExecutionStatus"
    ]
    """<p>The status of this specific execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExecutionResponse) -> dict:
    out: dict = {}
    if "execution_id" in value:
        out["ExecutionId"] = value["execution_id"]
    if "export" in value:
        import aws_sdk_bcm_data_exports.types.export

        out["Export"] = aws_sdk_bcm_data_exports.types.export.serialize_aws_json_1_1(
            value["export"]
        )
    if "execution_status" in value:
        import aws_sdk_bcm_data_exports.types.execution_status

        out["ExecutionStatus"] = (
            aws_sdk_bcm_data_exports.types.execution_status.serialize_aws_json_1_1(
                value["execution_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExecutionResponse:
    out: GetExecutionResponse = {}  # type: ignore[typeddict-item]
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    if "Export" in data:
        import aws_sdk_bcm_data_exports.types.export

        out["export"] = aws_sdk_bcm_data_exports.types.export.deserialize_aws_json_1_1(
            data["Export"]
        )
    if "ExecutionStatus" in data:
        import aws_sdk_bcm_data_exports.types.execution_status

        out["execution_status"] = (
            aws_sdk_bcm_data_exports.types.execution_status.deserialize_aws_json_1_1(
                data["ExecutionStatus"]
            )
        )
    return out
