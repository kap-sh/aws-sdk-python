"""Generated from Smithy shape ``com.amazonaws.comprehend#EntitiesDetectionJobProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.any_length_string
    import aws_sdk_comprehend.types.comprehend_arn
    import aws_sdk_comprehend.types.comprehend_flywheel_arn
    import aws_sdk_comprehend.types.entity_recognizer_arn
    import aws_sdk_comprehend.types.iam_role_arn
    import aws_sdk_comprehend.types.input_data_config
    import aws_sdk_comprehend.types.job_id
    import aws_sdk_comprehend.types.job_name
    import aws_sdk_comprehend.types.job_status
    import aws_sdk_comprehend.types.kms_key_id
    import aws_sdk_comprehend.types.language_code
    import aws_sdk_comprehend.types.output_data_config
    import aws_sdk_comprehend.types.timestamp
    import aws_sdk_comprehend.types.vpc_config


class EntitiesDetectionJobProperties(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_comprehend.types.job_id.JobId"]
    """<p>The identifier assigned to the entities detection job.</p>"""
    job_arn: NotRequired["aws_sdk_comprehend.types.comprehend_arn.ComprehendArn"]
    """<p>The Amazon Resource Name (ARN) of the entities detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:<partition>:comprehend:<region>:<account-id>:entities-detection-job/<job-id></code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>"""
    job_name: NotRequired["aws_sdk_comprehend.types.job_name.JobName"]
    """<p>The name that you assigned the entities detection job.</p>"""
    job_status: NotRequired["aws_sdk_comprehend.types.job_status.JobStatus"]
    """<p>The current status of the entities detection job. If the status is <code>FAILED</code>, the <code>Message</code> field shows the reason for the failure.</p>"""
    message: NotRequired["aws_sdk_comprehend.types.any_length_string.AnyLengthString"]
    """<p>A description of the status of a job.</p>"""
    submit_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the entities detection job was submitted for processing.</p>"""
    end_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the entities detection job completed</p>"""
    entity_recognizer_arn: NotRequired[
        "aws_sdk_comprehend.types.entity_recognizer_arn.EntityRecognizerArn"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the entity recognizer.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_comprehend.types.input_data_config.InputDataConfig"
    ]
    """<p>The input data configuration that you supplied when you created the entities detection job.</p>"""
    output_data_config: NotRequired[
        "aws_sdk_comprehend.types.output_data_config.OutputDataConfig"
    ]
    """<p>The output data configuration that you supplied when you created the entities detection job. </p>"""
    language_code: NotRequired["aws_sdk_comprehend.types.language_code.LanguageCode"]
    """<p>The language code of the input documents.</p>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_comprehend.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    volume_kms_key_id: NotRequired["aws_sdk_comprehend.types.kms_key_id.KmsKeyId"]
    r"""<p>ID for the Amazon Web Services Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:</p> <ul> <li> <p>KMS Key ID: <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>Amazon Resource Name (ARN) of a KMS Key: <code>\"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> </ul>"""
    vpc_config: NotRequired["aws_sdk_comprehend.types.vpc_config.VpcConfig"]
    r"""<p> Configuration parameters for a private Virtual Private Cloud (VPC) containing the resources you are using for your entity detection job. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html\">Amazon VPC</a>. </p>"""
    flywheel_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the flywheel associated with this job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitiesDetectionJobProperties) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_arn" in value:
        out["JobArn"] = value["job_arn"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import aws_sdk_comprehend.types.job_status

        out["JobStatus"] = aws_sdk_comprehend.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "submit_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["SubmitTime"] = aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["submit_time"]
        )
    if "end_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["EndTime"] = aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "entity_recognizer_arn" in value:
        out["EntityRecognizerArn"] = value["entity_recognizer_arn"]
    if "input_data_config" in value:
        import aws_sdk_comprehend.types.input_data_config

        out["InputDataConfig"] = (
            aws_sdk_comprehend.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import aws_sdk_comprehend.types.output_data_config

        out["OutputDataConfig"] = (
            aws_sdk_comprehend.types.output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "language_code" in value:
        import aws_sdk_comprehend.types.language_code

        out["LanguageCode"] = (
            aws_sdk_comprehend.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "vpc_config" in value:
        import aws_sdk_comprehend.types.vpc_config

        out["VpcConfig"] = aws_sdk_comprehend.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntitiesDetectionJobProperties:
    out: EntitiesDetectionJobProperties = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "JobArn" in data:
        out["job_arn"] = data["JobArn"]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobStatus" in data:
        import aws_sdk_comprehend.types.job_status

        out["job_status"] = (
            aws_sdk_comprehend.types.job_status.deserialize_aws_json_1_1(
                data["JobStatus"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "SubmitTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["submit_time"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["end_time"] = aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "EntityRecognizerArn" in data:
        out["entity_recognizer_arn"] = data["EntityRecognizerArn"]
    if "InputDataConfig" in data:
        import aws_sdk_comprehend.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_comprehend.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if "OutputDataConfig" in data:
        import aws_sdk_comprehend.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_comprehend.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if "LanguageCode" in data:
        import aws_sdk_comprehend.types.language_code

        out["language_code"] = (
            aws_sdk_comprehend.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "VolumeKmsKeyId" in data:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if "VpcConfig" in data:
        import aws_sdk_comprehend.types.vpc_config

        out["vpc_config"] = (
            aws_sdk_comprehend.types.vpc_config.deserialize_aws_json_1_1(
                data["VpcConfig"]
            )
        )
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    return out
