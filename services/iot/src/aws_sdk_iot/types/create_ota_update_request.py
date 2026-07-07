"""Generated from Smithy shape ``com.amazonaws.iot#CreateOTAUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.additional_parameter_map
    import aws_sdk_iot.types.aws_job_abort_config
    import aws_sdk_iot.types.aws_job_executions_rollout_config
    import aws_sdk_iot.types.aws_job_presigned_url_config
    import aws_sdk_iot.types.aws_job_timeout_config
    import aws_sdk_iot.types.ota_update_description
    import aws_sdk_iot.types.ota_update_files
    import aws_sdk_iot.types.ota_update_id
    import aws_sdk_iot.types.protocols
    import aws_sdk_iot.types.role_arn
    import aws_sdk_iot.types.tag_list
    import aws_sdk_iot.types.target_selection
    import aws_sdk_iot.types.targets


class CreateOTAUpdateRequest(TypedDict, closed=True):
    ota_update_id: "aws_sdk_iot.types.ota_update_id.OTAUpdateId"
    """<p>The ID of the OTA update to be created.</p>"""
    description: NotRequired[
        "aws_sdk_iot.types.ota_update_description.OTAUpdateDescription"
    ]
    """<p>The description of the OTA update.</p>"""
    targets: "aws_sdk_iot.types.targets.Targets"
    """<p>The devices targeted to receive OTA updates.</p>"""
    protocols: NotRequired["aws_sdk_iot.types.protocols.Protocols"]
    """<p>The protocol used to transfer the OTA update image. Valid values are [HTTP], [MQTT], [HTTP, MQTT]. When both HTTP and MQTT are specified, the target device can choose the protocol.</p>"""
    target_selection: NotRequired["aws_sdk_iot.types.target_selection.TargetSelection"]
    """<p>Specifies whether the update will continue to run (CONTINUOUS), or will be complete after all the things specified as targets have completed the update (SNAPSHOT). If continuous, the update may also be run on a thing when a change is detected in a target. For example, an update will run on a thing when the thing is added to a target group, even after the update was completed by all things originally in the group. Valid values: CONTINUOUS | SNAPSHOT.</p>"""
    aws_job_executions_rollout_config: NotRequired[
        "aws_sdk_iot.types.aws_job_executions_rollout_config.AwsJobExecutionsRolloutConfig"
    ]
    """<p>Configuration for the rollout of OTA updates.</p>"""
    aws_job_presigned_url_config: NotRequired[
        "aws_sdk_iot.types.aws_job_presigned_url_config.AwsJobPresignedUrlConfig"
    ]
    """<p>Configuration information for pre-signed URLs.</p>"""
    aws_job_abort_config: NotRequired[
        "aws_sdk_iot.types.aws_job_abort_config.AwsJobAbortConfig"
    ]
    """<p>The criteria that determine when and how a job abort takes place.</p>"""
    aws_job_timeout_config: NotRequired[
        "aws_sdk_iot.types.aws_job_timeout_config.AwsJobTimeoutConfig"
    ]
    """<p>Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to <code>IN_PROGRESS</code>. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to <code>TIMED_OUT</code>.</p>"""
    files: "aws_sdk_iot.types.ota_update_files.OTAUpdateFiles"
    """<p>The files to be streamed by the OTA update.</p>"""
    role_arn: "aws_sdk_iot.types.role_arn.RoleArn"
    """<p>The IAM role that grants Amazon Web Services IoT Core access to the Amazon S3, IoT jobs and Amazon Web Services Code Signing resources to create an OTA update job.</p>"""
    additional_parameters: NotRequired[
        "aws_sdk_iot.types.additional_parameter_map.AdditionalParameterMap"
    ]
    """<p>A list of additional OTA update parameters, which are name-value pairs. They won't be sent to devices as a part of the Job document.</p>"""
    tags: NotRequired["aws_sdk_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage updates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOTAUpdateRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_iot.types.targets

    out["targets"] = aws_sdk_iot.types.targets.serialize_json(value["targets"])
    if "protocols" in value:
        import aws_sdk_iot.types.protocols

        out["protocols"] = aws_sdk_iot.types.protocols.serialize_json(
            value["protocols"]
        )
    if "target_selection" in value:
        import aws_sdk_iot.types.target_selection

        out["targetSelection"] = aws_sdk_iot.types.target_selection.serialize_json(
            value["target_selection"]
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
    if "aws_job_abort_config" in value:
        import aws_sdk_iot.types.aws_job_abort_config

        out["awsJobAbortConfig"] = (
            aws_sdk_iot.types.aws_job_abort_config.serialize_json(
                value["aws_job_abort_config"]
            )
        )
    if "aws_job_timeout_config" in value:
        import aws_sdk_iot.types.aws_job_timeout_config

        out["awsJobTimeoutConfig"] = (
            aws_sdk_iot.types.aws_job_timeout_config.serialize_json(
                value["aws_job_timeout_config"]
            )
        )
    import aws_sdk_iot.types.ota_update_files

    out["files"] = aws_sdk_iot.types.ota_update_files.serialize_json(value["files"])
    out["roleArn"] = value["role_arn"]
    if "additional_parameters" in value:
        import aws_sdk_iot.types.additional_parameter_map

        out["additionalParameters"] = (
            aws_sdk_iot.types.additional_parameter_map.serialize_json(
                value["additional_parameters"]
            )
        )
    if "tags" in value:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateOTAUpdateRequest:
    out: CreateOTAUpdateRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "targets" in data:
        import aws_sdk_iot.types.targets

        out["targets"] = aws_sdk_iot.types.targets.deserialize_json(data["targets"])
    else:
        raise DeserializationError("CreateOTAUpdateRequest.targets required")
    if "protocols" in data:
        import aws_sdk_iot.types.protocols

        out["protocols"] = aws_sdk_iot.types.protocols.deserialize_json(
            data["protocols"]
        )
    if "targetSelection" in data:
        import aws_sdk_iot.types.target_selection

        out["target_selection"] = aws_sdk_iot.types.target_selection.deserialize_json(
            data["targetSelection"]
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
    if "awsJobAbortConfig" in data:
        import aws_sdk_iot.types.aws_job_abort_config

        out["aws_job_abort_config"] = (
            aws_sdk_iot.types.aws_job_abort_config.deserialize_json(
                data["awsJobAbortConfig"]
            )
        )
    if "awsJobTimeoutConfig" in data:
        import aws_sdk_iot.types.aws_job_timeout_config

        out["aws_job_timeout_config"] = (
            aws_sdk_iot.types.aws_job_timeout_config.deserialize_json(
                data["awsJobTimeoutConfig"]
            )
        )
    if "files" in data:
        import aws_sdk_iot.types.ota_update_files

        out["files"] = aws_sdk_iot.types.ota_update_files.deserialize_json(
            data["files"]
        )
    else:
        raise DeserializationError("CreateOTAUpdateRequest.files required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateOTAUpdateRequest.role_arn required")
    if "additionalParameters" in data:
        import aws_sdk_iot.types.additional_parameter_map

        out["additional_parameters"] = (
            aws_sdk_iot.types.additional_parameter_map.deserialize_json(
                data["additionalParameters"]
            )
        )
    if "tags" in data:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.deserialize_json(data["tags"])
    return out
