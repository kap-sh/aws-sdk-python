"""Generated from Smithy shape ``com.amazonaws.glue#GetDataQualityModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_model_status
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.timestamp


class GetDataQualityModelResponse(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_glue.types.data_quality_model_status.DataQualityModelStatus"
    ]
    """<p>The training status of the data quality model.</p>"""
    started_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The timestamp when the data quality model training started.</p>"""
    completed_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The timestamp when the data quality model training completed.</p>"""
    failure_reason: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The training failure reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataQualityModelResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_glue.types.data_quality_model_status

        out["Status"] = (
            aws_sdk_glue.types.data_quality_model_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "started_on" in value:
        import aws_sdk_glue.types.timestamp

        out["StartedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "completed_on" in value:
        import aws_sdk_glue.types.timestamp

        out["CompletedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["completed_on"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataQualityModelResponse:
    out: GetDataQualityModelResponse = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_glue.types.data_quality_model_status

        out["status"] = (
            aws_sdk_glue.types.data_quality_model_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StartedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["started_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if "CompletedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["completed_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CompletedOn"]
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
