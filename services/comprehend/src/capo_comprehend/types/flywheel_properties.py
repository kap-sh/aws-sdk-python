"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.any_length_string
    import capo_comprehend.types.comprehend_flywheel_arn
    import capo_comprehend.types.comprehend_model_arn
    import capo_comprehend.types.data_security_config
    import capo_comprehend.types.flywheel_iteration_id
    import capo_comprehend.types.flywheel_status
    import capo_comprehend.types.iam_role_arn
    import capo_comprehend.types.model_type
    import capo_comprehend.types.s3_uri
    import capo_comprehend.types.task_config
    import capo_comprehend.types.timestamp


class FlywheelProperties(TypedDict, closed=True):
    flywheel_arn: NotRequired[
        "capo_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the flywheel.</p>"""
    active_model_arn: NotRequired[
        "capo_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the active model version.</p>"""
    data_access_role_arn: NotRequired["capo_comprehend.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend permission to access the flywheel data.</p>"""
    task_config: NotRequired["capo_comprehend.types.task_config.TaskConfig"]
    """<p>Configuration about the model associated with a flywheel.</p>"""
    data_lake_s3_uri: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p>Amazon S3 URI of the data lake location. </p>"""
    data_security_config: NotRequired[
        "capo_comprehend.types.data_security_config.DataSecurityConfig"
    ]
    """<p>Data security configuration.</p>"""
    status: NotRequired["capo_comprehend.types.flywheel_status.FlywheelStatus"]
    """<p>The status of the flywheel.</p>"""
    model_type: NotRequired["capo_comprehend.types.model_type.ModelType"]
    """<p>Model type of the flywheel's model.</p>"""
    message: NotRequired["capo_comprehend.types.any_length_string.AnyLengthString"]
    """<p>A description of the status of the flywheel.</p>"""
    creation_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Creation time of the flywheel.</p>"""
    last_modified_time: NotRequired["capo_comprehend.types.timestamp.Timestamp"]
    """<p>Last modified time for the flywheel.</p>"""
    latest_flywheel_iteration: NotRequired[
        "capo_comprehend.types.flywheel_iteration_id.FlywheelIterationId"
    ]
    """<p>The most recent flywheel iteration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelProperties) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "active_model_arn" in value:
        out["ActiveModelArn"] = value["active_model_arn"]
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "task_config" in value:
        import capo_comprehend.types.task_config

        out["TaskConfig"] = capo_comprehend.types.task_config.serialize_aws_json_1_1(
            value["task_config"]
        )
    if "data_lake_s3_uri" in value:
        out["DataLakeS3Uri"] = value["data_lake_s3_uri"]
    if "data_security_config" in value:
        import capo_comprehend.types.data_security_config

        out["DataSecurityConfig"] = (
            capo_comprehend.types.data_security_config.serialize_aws_json_1_1(
                value["data_security_config"]
            )
        )
    if "status" in value:
        import capo_comprehend.types.flywheel_status

        out["Status"] = capo_comprehend.types.flywheel_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "model_type" in value:
        import capo_comprehend.types.model_type

        out["ModelType"] = capo_comprehend.types.model_type.serialize_aws_json_1_1(
            value["model_type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "creation_time" in value:
        import capo_comprehend.types.timestamp

        out["CreationTime"] = capo_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_comprehend.types.timestamp

        out["LastModifiedTime"] = (
            capo_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "latest_flywheel_iteration" in value:
        out["LatestFlywheelIteration"] = value["latest_flywheel_iteration"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlywheelProperties:
    out: FlywheelProperties = {}  # type: ignore[typeddict-item]
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    if "ActiveModelArn" in data:
        out["active_model_arn"] = data["ActiveModelArn"]
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "TaskConfig" in data:
        import capo_comprehend.types.task_config

        out["task_config"] = capo_comprehend.types.task_config.deserialize_aws_json_1_1(
            data["TaskConfig"]
        )
    if "DataLakeS3Uri" in data:
        out["data_lake_s3_uri"] = data["DataLakeS3Uri"]
    if "DataSecurityConfig" in data:
        import capo_comprehend.types.data_security_config

        out["data_security_config"] = (
            capo_comprehend.types.data_security_config.deserialize_aws_json_1_1(
                data["DataSecurityConfig"]
            )
        )
    if "Status" in data:
        import capo_comprehend.types.flywheel_status

        out["status"] = capo_comprehend.types.flywheel_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ModelType" in data:
        import capo_comprehend.types.model_type

        out["model_type"] = capo_comprehend.types.model_type.deserialize_aws_json_1_1(
            data["ModelType"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "CreationTime" in data:
        import capo_comprehend.types.timestamp

        out["creation_time"] = capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_comprehend.types.timestamp

        out["last_modified_time"] = (
            capo_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LatestFlywheelIteration" in data:
        out["latest_flywheel_iteration"] = data["LatestFlywheelIteration"]
    return out
