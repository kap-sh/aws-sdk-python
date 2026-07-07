"""Generated from Smithy shape ``com.amazonaws.comprehend#PiiEntitiesDetectionJobProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.any_length_string
    import aws_sdk_comprehend.types.comprehend_arn
    import aws_sdk_comprehend.types.iam_role_arn
    import aws_sdk_comprehend.types.input_data_config
    import aws_sdk_comprehend.types.job_id
    import aws_sdk_comprehend.types.job_name
    import aws_sdk_comprehend.types.job_status
    import aws_sdk_comprehend.types.language_code
    import aws_sdk_comprehend.types.pii_entities_detection_mode
    import aws_sdk_comprehend.types.pii_output_data_config
    import aws_sdk_comprehend.types.redaction_config
    import aws_sdk_comprehend.types.timestamp


class PiiEntitiesDetectionJobProperties(TypedDict, closed=True):
    job_id: NotRequired["aws_sdk_comprehend.types.job_id.JobId"]
    """<p>The identifier assigned to the PII entities detection job.</p>"""
    job_arn: NotRequired["aws_sdk_comprehend.types.comprehend_arn.ComprehendArn"]
    """<p>The Amazon Resource Name (ARN) of the PII entities detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:<partition>:comprehend:<region>:<account-id>:pii-entities-detection-job/<job-id></code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>"""
    job_name: NotRequired["aws_sdk_comprehend.types.job_name.JobName"]
    """<p>The name that you assigned the PII entities detection job.</p>"""
    job_status: NotRequired["aws_sdk_comprehend.types.job_status.JobStatus"]
    """<p>The current status of the PII entities detection job. If the status is <code>FAILED</code>, the <code>Message</code> field shows the reason for the failure.</p>"""
    message: NotRequired["aws_sdk_comprehend.types.any_length_string.AnyLengthString"]
    """<p>A description of the status of a job.</p>"""
    submit_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the PII entities detection job was submitted for processing.</p>"""
    end_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the PII entities detection job completed.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_comprehend.types.input_data_config.InputDataConfig"
    ]
    """<p>The input properties for a PII entities detection job.</p>"""
    output_data_config: NotRequired[
        "aws_sdk_comprehend.types.pii_output_data_config.PiiOutputDataConfig"
    ]
    """<p>The output data configuration that you supplied when you created the PII entities detection job.</p>"""
    redaction_config: NotRequired[
        "aws_sdk_comprehend.types.redaction_config.RedactionConfig"
    ]
    """<p>Provides configuration parameters for PII entity redaction.</p> <p>This parameter is required if you set the <code>Mode</code> parameter to <code>ONLY_REDACTION</code>. In that case, you must provide a <code>RedactionConfig</code> definition that includes the <code>PiiEntityTypes</code> parameter.</p>"""
    language_code: NotRequired["aws_sdk_comprehend.types.language_code.LanguageCode"]
    """<p>The language code of the input documents.</p>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_comprehend.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    mode: NotRequired[
        "aws_sdk_comprehend.types.pii_entities_detection_mode.PiiEntitiesDetectionMode"
    ]
    """<p>Specifies whether the output provides the locations (offsets) of PII entities or a file in which PII entities are redacted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PiiEntitiesDetectionJobProperties) -> dict:
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
    if "input_data_config" in value:
        import aws_sdk_comprehend.types.input_data_config

        out["InputDataConfig"] = (
            aws_sdk_comprehend.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import aws_sdk_comprehend.types.pii_output_data_config

        out["OutputDataConfig"] = (
            aws_sdk_comprehend.types.pii_output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "redaction_config" in value:
        import aws_sdk_comprehend.types.redaction_config

        out["RedactionConfig"] = (
            aws_sdk_comprehend.types.redaction_config.serialize_aws_json_1_1(
                value["redaction_config"]
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
    if "mode" in value:
        import aws_sdk_comprehend.types.pii_entities_detection_mode

        out["Mode"] = (
            aws_sdk_comprehend.types.pii_entities_detection_mode.serialize_aws_json_1_1(
                value["mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PiiEntitiesDetectionJobProperties:
    out: PiiEntitiesDetectionJobProperties = {}  # type: ignore[typeddict-item]
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
    if "InputDataConfig" in data:
        import aws_sdk_comprehend.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_comprehend.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if "OutputDataConfig" in data:
        import aws_sdk_comprehend.types.pii_output_data_config

        out["output_data_config"] = (
            aws_sdk_comprehend.types.pii_output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if "RedactionConfig" in data:
        import aws_sdk_comprehend.types.redaction_config

        out["redaction_config"] = (
            aws_sdk_comprehend.types.redaction_config.deserialize_aws_json_1_1(
                data["RedactionConfig"]
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
    if "Mode" in data:
        import aws_sdk_comprehend.types.pii_entities_detection_mode

        out["mode"] = (
            aws_sdk_comprehend.types.pii_entities_detection_mode.deserialize_aws_json_1_1(
                data["Mode"]
            )
        )
    return out
