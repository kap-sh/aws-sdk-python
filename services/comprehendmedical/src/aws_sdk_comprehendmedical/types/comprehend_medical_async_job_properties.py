"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ComprehendMedicalAsyncJobProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.any_length_string
    import aws_sdk_comprehendmedical.types.iam_role_arn
    import aws_sdk_comprehendmedical.types.input_data_config
    import aws_sdk_comprehendmedical.types.job_id
    import aws_sdk_comprehendmedical.types.job_name
    import aws_sdk_comprehendmedical.types.job_status
    import aws_sdk_comprehendmedical.types.kms_key
    import aws_sdk_comprehendmedical.types.language_code
    import aws_sdk_comprehendmedical.types.manifest_file_path
    import aws_sdk_comprehendmedical.types.model_version
    import aws_sdk_comprehendmedical.types.output_data_config
    import aws_sdk_comprehendmedical.types.timestamp


class ComprehendMedicalAsyncJobProperties(TypedDict):
    job_id: NotRequired["aws_sdk_comprehendmedical.types.job_id.JobId"]
    """<p>The identifier assigned to the detection job.</p>"""
    job_name: NotRequired["aws_sdk_comprehendmedical.types.job_name.JobName"]
    """<p>The name that you assigned to the detection job.</p>"""
    job_status: NotRequired["aws_sdk_comprehendmedical.types.job_status.JobStatus"]
    """<p>The current status of the detection job. If the status is <code>FAILED</code>, the <code>Message</code> field shows the reason for the failure.</p>"""
    message: NotRequired[
        "aws_sdk_comprehendmedical.types.any_length_string.AnyLengthString"
    ]
    """<p>A description of the status of a job.</p>"""
    submit_time: NotRequired["aws_sdk_comprehendmedical.types.timestamp.Timestamp"]
    """<p>The time that the detection job was submitted for processing.</p>"""
    end_time: NotRequired["aws_sdk_comprehendmedical.types.timestamp.Timestamp"]
    """<p>The time that the detection job completed.</p>"""
    expiration_time: NotRequired["aws_sdk_comprehendmedical.types.timestamp.Timestamp"]
    """<p>The date and time that job metadata is deleted from the server. Output files in your S3 bucket will not be deleted. After the metadata is deleted, the job will no longer appear in the results of the <code>ListEntitiesDetectionV2Job</code> or the <code>ListPHIDetectionJobs</code> operation.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_comprehendmedical.types.input_data_config.InputDataConfig"
    ]
    """<p>The input data configuration that you supplied when you created the detection job.</p>"""
    output_data_config: NotRequired[
        "aws_sdk_comprehendmedical.types.output_data_config.OutputDataConfig"
    ]
    """<p>The output data configuration that you supplied when you created the detection job.</p>"""
    language_code: NotRequired[
        "aws_sdk_comprehendmedical.types.language_code.LanguageCode"
    ]
    """<p>The language code of the input documents.</p>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_comprehendmedical.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) that gives Amazon Comprehend Medical read access to your input data.</p>"""
    manifest_file_path: NotRequired[
        "aws_sdk_comprehendmedical.types.manifest_file_path.ManifestFilePath"
    ]
    """<p>The path to the file that describes the results of a batch job.</p>"""
    kms_key: NotRequired["aws_sdk_comprehendmedical.types.kms_key.KMSKey"]
    """<p>The AWS Key Management Service key, if any, used to encrypt the output files. </p>"""
    model_version: NotRequired[
        "aws_sdk_comprehendmedical.types.model_version.ModelVersion"
    ]
    """<p>The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComprehendMedicalAsyncJobProperties) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import aws_sdk_comprehendmedical.types.job_status

        out["JobStatus"] = (
            aws_sdk_comprehendmedical.types.job_status.serialize_aws_json_1_1(
                value["job_status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "submit_time" in value:
        import aws_sdk_comprehendmedical.types.timestamp

        out["SubmitTime"] = (
            aws_sdk_comprehendmedical.types.timestamp.serialize_aws_json_1_1(
                value["submit_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_comprehendmedical.types.timestamp

        out["EndTime"] = (
            aws_sdk_comprehendmedical.types.timestamp.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "expiration_time" in value:
        import aws_sdk_comprehendmedical.types.timestamp

        out["ExpirationTime"] = (
            aws_sdk_comprehendmedical.types.timestamp.serialize_aws_json_1_1(
                value["expiration_time"]
            )
        )
    if "input_data_config" in value:
        import aws_sdk_comprehendmedical.types.input_data_config

        out["InputDataConfig"] = (
            aws_sdk_comprehendmedical.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import aws_sdk_comprehendmedical.types.output_data_config

        out["OutputDataConfig"] = (
            aws_sdk_comprehendmedical.types.output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "language_code" in value:
        import aws_sdk_comprehendmedical.types.language_code

        out["LanguageCode"] = (
            aws_sdk_comprehendmedical.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "manifest_file_path" in value:
        out["ManifestFilePath"] = value["manifest_file_path"]
    if "kms_key" in value:
        out["KMSKey"] = value["kms_key"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComprehendMedicalAsyncJobProperties:
    out: ComprehendMedicalAsyncJobProperties = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobStatus" in data:
        import aws_sdk_comprehendmedical.types.job_status

        out["job_status"] = (
            aws_sdk_comprehendmedical.types.job_status.deserialize_aws_json_1_1(
                data["JobStatus"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "SubmitTime" in data:
        import aws_sdk_comprehendmedical.types.timestamp

        out["submit_time"] = (
            aws_sdk_comprehendmedical.types.timestamp.deserialize_aws_json_1_1(
                data["SubmitTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_comprehendmedical.types.timestamp

        out["end_time"] = (
            aws_sdk_comprehendmedical.types.timestamp.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if "ExpirationTime" in data:
        import aws_sdk_comprehendmedical.types.timestamp

        out["expiration_time"] = (
            aws_sdk_comprehendmedical.types.timestamp.deserialize_aws_json_1_1(
                data["ExpirationTime"]
            )
        )
    if "InputDataConfig" in data:
        import aws_sdk_comprehendmedical.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_comprehendmedical.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if "OutputDataConfig" in data:
        import aws_sdk_comprehendmedical.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_comprehendmedical.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if "LanguageCode" in data:
        import aws_sdk_comprehendmedical.types.language_code

        out["language_code"] = (
            aws_sdk_comprehendmedical.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "ManifestFilePath" in data:
        out["manifest_file_path"] = data["ManifestFilePath"]
    if "KMSKey" in data:
        out["kms_key"] = data["KMSKey"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    return out
