"""Generated from Smithy shape ``com.amazonaws.iot#CreateOTAUpdateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_iot_job_arn
    import capo_iot.types.aws_iot_job_id
    import capo_iot.types.ota_update_arn
    import capo_iot.types.ota_update_id
    import capo_iot.types.ota_update_status


class CreateOTAUpdateResponse(TypedDict, closed=True):
    ota_update_id: NotRequired["capo_iot.types.ota_update_id.OTAUpdateId"]
    """<p>The OTA update ID.</p>"""
    aws_iot_job_id: NotRequired["capo_iot.types.aws_iot_job_id.AwsIotJobId"]
    """<p>The IoT job ID associated with the OTA update.</p>"""
    ota_update_arn: NotRequired["capo_iot.types.ota_update_arn.OTAUpdateArn"]
    """<p>The OTA update ARN.</p>"""
    aws_iot_job_arn: NotRequired["capo_iot.types.aws_iot_job_arn.AwsIotJobArn"]
    """<p>The IoT job ARN associated with the OTA update.</p>"""
    ota_update_status: NotRequired["capo_iot.types.ota_update_status.OTAUpdateStatus"]
    """<p>The OTA update status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOTAUpdateResponse) -> dict:
    out: dict = {}
    if "ota_update_id" in value:
        out["otaUpdateId"] = value["ota_update_id"]
    if "aws_iot_job_id" in value:
        out["awsIotJobId"] = value["aws_iot_job_id"]
    if "ota_update_arn" in value:
        out["otaUpdateArn"] = value["ota_update_arn"]
    if "aws_iot_job_arn" in value:
        out["awsIotJobArn"] = value["aws_iot_job_arn"]
    if "ota_update_status" in value:
        import capo_iot.types.ota_update_status

        out["otaUpdateStatus"] = capo_iot.types.ota_update_status.serialize_json(
            value["ota_update_status"]
        )
    return out


def deserialize_json(data: dict) -> CreateOTAUpdateResponse:
    out: CreateOTAUpdateResponse = {}  # type: ignore[typeddict-item]
    if "otaUpdateId" in data:
        out["ota_update_id"] = data["otaUpdateId"]
    if "awsIotJobId" in data:
        out["aws_iot_job_id"] = data["awsIotJobId"]
    if "otaUpdateArn" in data:
        out["ota_update_arn"] = data["otaUpdateArn"]
    if "awsIotJobArn" in data:
        out["aws_iot_job_arn"] = data["awsIotJobArn"]
    if "otaUpdateStatus" in data:
        import capo_iot.types.ota_update_status

        out["ota_update_status"] = capo_iot.types.ota_update_status.deserialize_json(
            data["otaUpdateStatus"]
        )
    return out
