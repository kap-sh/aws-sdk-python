"""Generated from Smithy shape ``com.amazonaws.comprehend#EventsDetectionJobProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.any_length_string
    import aws_sdk_comprehend.types.comprehend_arn
    import aws_sdk_comprehend.types.iam_role_arn
    import aws_sdk_comprehend.types.input_data_config
    import aws_sdk_comprehend.types.job_id
    import aws_sdk_comprehend.types.job_name
    import aws_sdk_comprehend.types.job_status
    import aws_sdk_comprehend.types.language_code
    import aws_sdk_comprehend.types.output_data_config
    import aws_sdk_comprehend.types.target_event_types
    import aws_sdk_comprehend.types.timestamp


class EventsDetectionJobProperties(TypedDict):
    job_id: NotRequired["aws_sdk_comprehend.types.job_id.JobId"]
    """<p>The identifier assigned to the events detection job.</p>"""
    job_arn: NotRequired["aws_sdk_comprehend.types.comprehend_arn.ComprehendArn"]
    """<p>The Amazon Resource Name (ARN) of the events detection job. It is a unique, fully qualified identifier for the job. It includes the Amazon Web Services account, Amazon Web Services Region, and the job ID. The format of the ARN is as follows:</p> <p> <code>arn:<partition>:comprehend:<region>:<account-id>:events-detection-job/<job-id></code> </p> <p>The following is an example job ARN:</p> <p> <code>arn:aws:comprehend:us-west-2:111122223333:events-detection-job/1234abcd12ab34cd56ef1234567890ab</code> </p>"""
    job_name: NotRequired["aws_sdk_comprehend.types.job_name.JobName"]
    """<p>The name you assigned the events detection job.</p>"""
    job_status: NotRequired["aws_sdk_comprehend.types.job_status.JobStatus"]
    """<p>The current status of the events detection job.</p>"""
    message: NotRequired["aws_sdk_comprehend.types.any_length_string.AnyLengthString"]
    """<p>A description of the status of the events detection job.</p>"""
    submit_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the events detection job was submitted for processing.</p>"""
    end_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The time that the events detection job completed.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_comprehend.types.input_data_config.InputDataConfig"
    ]
    """<p>The input data configuration that you supplied when you created the events detection job.</p>"""
    output_data_config: NotRequired[
        "aws_sdk_comprehend.types.output_data_config.OutputDataConfig"
    ]
    """<p>The output data configuration that you supplied when you created the events detection job.</p>"""
    language_code: NotRequired["aws_sdk_comprehend.types.language_code.LanguageCode"]
    """<p>The language code of the input documents.</p>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_comprehend.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.</p>"""
    target_event_types: NotRequired[
        "aws_sdk_comprehend.types.target_event_types.TargetEventTypes"
    ]
    """<p>The types of events that are detected by the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventsDetectionJobProperties) -> dict:
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
    if "target_event_types" in value:
        import aws_sdk_comprehend.types.target_event_types

        out["TargetEventTypes"] = (
            aws_sdk_comprehend.types.target_event_types.serialize_aws_json_1_1(
                value["target_event_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventsDetectionJobProperties:
    out: EventsDetectionJobProperties = {}  # type: ignore[typeddict-item]
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
    if "TargetEventTypes" in data:
        import aws_sdk_comprehend.types.target_event_types

        out["target_event_types"] = (
            aws_sdk_comprehend.types.target_event_types.deserialize_aws_json_1_1(
                data["TargetEventTypes"]
            )
        )
    return out
