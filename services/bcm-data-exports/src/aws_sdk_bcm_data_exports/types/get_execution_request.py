"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#GetExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.arn
    import aws_sdk_bcm_data_exports.types.generic_string


class GetExecutionRequest(TypedDict):
    export_arn: "aws_sdk_bcm_data_exports.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Export object that generated this specific execution.</p>"""
    execution_id: "aws_sdk_bcm_data_exports.types.generic_string.GenericString"
    """<p>The ID for this specific execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExecutionRequest) -> dict:
    out: dict = {}
    out["ExportArn"] = value["export_arn"]
    out["ExecutionId"] = value["execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExecutionRequest:
    out: GetExecutionRequest = {}  # type: ignore[typeddict-item]
    if "ExportArn" in data:
        out["export_arn"] = data["ExportArn"]
    else:
        raise DeserializationError("GetExecutionRequest.export_arn required")
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    else:
        raise DeserializationError("GetExecutionRequest.execution_id required")
    return out
