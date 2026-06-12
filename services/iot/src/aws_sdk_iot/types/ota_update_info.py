"""Generated from Smithy shape ``com.amazonaws.iot#OTAUpdateInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.additional_parameter_map
    import aws_sdk_iot.types.aws_iot_job_arn
    import aws_sdk_iot.types.aws_iot_job_id
    import aws_sdk_iot.types.aws_job_executions_rollout_config
    import aws_sdk_iot.types.aws_job_presigned_url_config
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.error_info
    import aws_sdk_iot.types.ota_update_arn
    import aws_sdk_iot.types.ota_update_description
    import aws_sdk_iot.types.ota_update_files
    import aws_sdk_iot.types.ota_update_id
    import aws_sdk_iot.types.ota_update_status
    import aws_sdk_iot.types.protocols
    import aws_sdk_iot.types.target_selection
    import aws_sdk_iot.types.targets


class OTAUpdateInfo(TypedDict):
    ota_update_id: NotRequired["aws_sdk_iot.types.ota_update_id.OTAUpdateId"]
    """<p>The OTA update ID.</p>"""
    ota_update_arn: NotRequired["aws_sdk_iot.types.ota_update_arn.OTAUpdateArn"]
    """<p>The OTA update ARN.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date when the OTA update was created.</p>"""
    last_modified_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date when the OTA update was last updated.</p>"""
    description: NotRequired[
        "aws_sdk_iot.types.ota_update_description.OTAUpdateDescription"
    ]
    """<p>A description of the OTA update.</p>"""
    targets: NotRequired["aws_sdk_iot.types.targets.Targets"]
    """<p>The targets of the OTA update.</p>"""
    protocols: NotRequired["aws_sdk_iot.types.protocols.Protocols"]
    """<p>The protocol used to transfer the OTA update image. Valid values are [HTTP], [MQTT], [HTTP, MQTT]. When both HTTP and MQTT are specified, the target device can choose the protocol.</p>"""
    aws_job_executions_rollout_config: NotRequired[
        "aws_sdk_iot.types.aws_job_executions_rollout_config.AwsJobExecutionsRolloutConfig"
    ]
    """<p>Configuration for the rollout of OTA updates.</p>"""
    aws_job_presigned_url_config: NotRequired[
        "aws_sdk_iot.types.aws_job_presigned_url_config.AwsJobPresignedUrlConfig"
    ]
    """<p>Configuration information for pre-signed URLs. Valid when <code>protocols</code> contains HTTP.</p>"""
    target_selection: NotRequired["aws_sdk_iot.types.target_selection.TargetSelection"]
    """<p>Specifies whether the OTA update will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the OTA update (SNAPSHOT). If continuous, the OTA update may also be run on a thing when a change is detected in a target. For example, an OTA update will run on a thing when the thing is added to a target group, even after the OTA update was completed by all things originally in the group. </p>"""
    ota_update_files: NotRequired["aws_sdk_iot.types.ota_update_files.OTAUpdateFiles"]
    """<p>A list of files associated with the OTA update.</p>"""
    ota_update_status: NotRequired[
        "aws_sdk_iot.types.ota_update_status.OTAUpdateStatus"
    ]
    """<p>The status of the OTA update.</p>"""
    aws_iot_job_id: NotRequired["aws_sdk_iot.types.aws_iot_job_id.AwsIotJobId"]
    """<p>The IoT job ID associated with the OTA update.</p>"""
    aws_iot_job_arn: NotRequired["aws_sdk_iot.types.aws_iot_job_arn.AwsIotJobArn"]
    """<p>The IoT job ARN associated with the OTA update.</p>"""
    error_info: NotRequired["aws_sdk_iot.types.error_info.ErrorInfo"]
    """<p>Error information associated with the OTA update.</p>"""
    additional_parameters: NotRequired[
        "aws_sdk_iot.types.additional_parameter_map.AdditionalParameterMap"
    ]
    """<p>A collection of name/value pairs</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OTAUpdateInfo) -> dict:
    out: dict = {}
    if "ota_update_id" in value:
        out["otaUpdateId"] = value["ota_update_id"]
    if "ota_update_arn" in value:
        out["otaUpdateArn"] = value["ota_update_arn"]
    if "creation_date" in value:
        import aws_sdk_iot.types.date_type

        out["creationDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    if "last_modified_date" in value:
        import aws_sdk_iot.types.date_type

        out["lastModifiedDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_modified_date"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "targets" in value:
        import aws_sdk_iot.types.targets

        out["targets"] = aws_sdk_iot.types.targets.serialize_json(value["targets"])
    if "protocols" in value:
        import aws_sdk_iot.types.protocols

        out["protocols"] = aws_sdk_iot.types.protocols.serialize_json(
            value["protocols"]
        )
    if "aws_job_executions_rollout_config" in value:
        import aws_sdk_iot.types.aws_job_executions_rollout_config

        out["awsJobExecutionsRolloutConfig"] = (
            aws_sdk_iot.types.aws_job_executions_rollout_config.serialize_json(
                value["aws_job_executions_rollout_config"]
            )
        )
    if "aws_job_presigned_url_config" in value:
        import aws_sdk_iot.types.aws_job_presigned_url_config

        out["awsJobPresignedUrlConfig"] = (
            aws_sdk_iot.types.aws_job_presigned_url_config.serialize_json(
                value["aws_job_presigned_url_config"]
            )
        )
    if "target_selection" in value:
        import aws_sdk_iot.types.target_selection

        out["targetSelection"] = aws_sdk_iot.types.target_selection.serialize_json(
            value["target_selection"]
        )
    if "ota_update_files" in value:
        import aws_sdk_iot.types.ota_update_files

        out["otaUpdateFiles"] = aws_sdk_iot.types.ota_update_files.serialize_json(
            value["ota_update_files"]
        )
    if "ota_update_status" in value:
        import aws_sdk_iot.types.ota_update_status

        out["otaUpdateStatus"] = aws_sdk_iot.types.ota_update_status.serialize_json(
            value["ota_update_status"]
        )
    if "aws_iot_job_id" in value:
        out["awsIotJobId"] = value["aws_iot_job_id"]
    if "aws_iot_job_arn" in value:
        out["awsIotJobArn"] = value["aws_iot_job_arn"]
    if "error_info" in value:
        import aws_sdk_iot.types.error_info

        out["errorInfo"] = aws_sdk_iot.types.error_info.serialize_json(
            value["error_info"]
        )
    if "additional_parameters" in value:
        import aws_sdk_iot.types.additional_parameter_map

        out["additionalParameters"] = (
            aws_sdk_iot.types.additional_parameter_map.serialize_json(
                value["additional_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> OTAUpdateInfo:
    out: OTAUpdateInfo = {}  # type: ignore[typeddict-item]
    if "otaUpdateId" in data:
        out["ota_update_id"] = data["otaUpdateId"]
    if "otaUpdateArn" in data:
        out["ota_update_arn"] = data["otaUpdateArn"]
    if "creationDate" in data:
        import aws_sdk_iot.types.date_type

        out["creation_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    if "lastModifiedDate" in data:
        import aws_sdk_iot.types.date_type

        out["last_modified_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastModifiedDate"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "targets" in data:
        import aws_sdk_iot.types.targets

        out["targets"] = aws_sdk_iot.types.targets.deserialize_json(data["targets"])
    if "protocols" in data:
        import aws_sdk_iot.types.protocols

        out["protocols"] = aws_sdk_iot.types.protocols.deserialize_json(
            data["protocols"]
        )
    if "awsJobExecutionsRolloutConfig" in data:
        import aws_sdk_iot.types.aws_job_executions_rollout_config

        out["aws_job_executions_rollout_config"] = (
            aws_sdk_iot.types.aws_job_executions_rollout_config.deserialize_json(
                data["awsJobExecutionsRolloutConfig"]
            )
        )
    if "awsJobPresignedUrlConfig" in data:
        import aws_sdk_iot.types.aws_job_presigned_url_config

        out["aws_job_presigned_url_config"] = (
            aws_sdk_iot.types.aws_job_presigned_url_config.deserialize_json(
                data["awsJobPresignedUrlConfig"]
            )
        )
    if "targetSelection" in data:
        import aws_sdk_iot.types.target_selection

        out["target_selection"] = aws_sdk_iot.types.target_selection.deserialize_json(
            data["targetSelection"]
        )
    if "otaUpdateFiles" in data:
        import aws_sdk_iot.types.ota_update_files

        out["ota_update_files"] = aws_sdk_iot.types.ota_update_files.deserialize_json(
            data["otaUpdateFiles"]
        )
    if "otaUpdateStatus" in data:
        import aws_sdk_iot.types.ota_update_status

        out["ota_update_status"] = aws_sdk_iot.types.ota_update_status.deserialize_json(
            data["otaUpdateStatus"]
        )
    if "awsIotJobId" in data:
        out["aws_iot_job_id"] = data["awsIotJobId"]
    if "awsIotJobArn" in data:
        out["aws_iot_job_arn"] = data["awsIotJobArn"]
    if "errorInfo" in data:
        import aws_sdk_iot.types.error_info

        out["error_info"] = aws_sdk_iot.types.error_info.deserialize_json(
            data["errorInfo"]
        )
    if "additionalParameters" in data:
        import aws_sdk_iot.types.additional_parameter_map

        out["additional_parameters"] = (
            aws_sdk_iot.types.additional_parameter_map.deserialize_json(
                data["additionalParameters"]
            )
        )
    return out
