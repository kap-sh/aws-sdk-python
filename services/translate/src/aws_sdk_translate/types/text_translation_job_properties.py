"""Generated from Smithy shape ``com.amazonaws.translate#TextTranslationJobProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_translate.types.iam_role_arn
    import aws_sdk_translate.types.input_data_config
    import aws_sdk_translate.types.job_details
    import aws_sdk_translate.types.job_id
    import aws_sdk_translate.types.job_name
    import aws_sdk_translate.types.job_status
    import aws_sdk_translate.types.language_code_string
    import aws_sdk_translate.types.output_data_config
    import aws_sdk_translate.types.resource_name_list
    import aws_sdk_translate.types.target_language_code_string_list
    import aws_sdk_translate.types.timestamp
    import aws_sdk_translate.types.translation_settings
    import aws_sdk_translate.types.unbounded_length_string


class TextTranslationJobProperties(TypedDict):
    job_id: NotRequired["aws_sdk_translate.types.job_id.JobId"]
    """<p>The ID of the translation job.</p>"""
    job_name: NotRequired["aws_sdk_translate.types.job_name.JobName"]
    """<p>The user-defined name of the translation job.</p>"""
    job_status: NotRequired["aws_sdk_translate.types.job_status.JobStatus"]
    """<p>The status of the translation job.</p>"""
    job_details: NotRequired["aws_sdk_translate.types.job_details.JobDetails"]
    """<p>The number of documents successfully and unsuccessfully processed during the translation job.</p>"""
    source_language_code: NotRequired[
        "aws_sdk_translate.types.language_code_string.LanguageCodeString"
    ]
    """<p>The language code of the language of the source text. The language must be a language supported by Amazon Translate.</p>"""
    target_language_codes: NotRequired[
        "aws_sdk_translate.types.target_language_code_string_list.TargetLanguageCodeStringList"
    ]
    """<p>The language code of the language of the target text. The language must be a language supported by Amazon Translate.</p>"""
    terminology_names: NotRequired[
        "aws_sdk_translate.types.resource_name_list.ResourceNameList"
    ]
    """<p>A list containing the names of the terminologies applied to a translation job. Only one terminology can be applied per <a>StartTextTranslationJob</a> request at this time.</p>"""
    parallel_data_names: NotRequired[
        "aws_sdk_translate.types.resource_name_list.ResourceNameList"
    ]
    """<p>A list containing the names of the parallel data resources applied to the translation job.</p>"""
    message: NotRequired[
        "aws_sdk_translate.types.unbounded_length_string.UnboundedLengthString"
    ]
    """<p>An explanation of any errors that may have occurred during the translation job.</p>"""
    submitted_time: NotRequired["aws_sdk_translate.types.timestamp.Timestamp"]
    """<p>The time at which the translation job was submitted.</p>"""
    end_time: NotRequired["aws_sdk_translate.types.timestamp.Timestamp"]
    """<p>The time at which the translation job ended.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_translate.types.input_data_config.InputDataConfig"
    ]
    """<p>The input configuration properties that were specified when the job was requested.</p>"""
    output_data_config: NotRequired[
        "aws_sdk_translate.types.output_data_config.OutputDataConfig"
    ]
    """<p>The output configuration properties that were specified when the job was requested.</p>"""
    data_access_role_arn: NotRequired["aws_sdk_translate.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of an AWS Identity Access and Management (IAM) role that granted Amazon Translate read access to the job's input data.</p>"""
    settings: NotRequired[
        "aws_sdk_translate.types.translation_settings.TranslationSettings"
    ]
    """<p>Settings that modify the translation output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextTranslationJobProperties) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import aws_sdk_translate.types.job_status

        out["JobStatus"] = aws_sdk_translate.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    if "job_details" in value:
        import aws_sdk_translate.types.job_details

        out["JobDetails"] = aws_sdk_translate.types.job_details.serialize_aws_json_1_1(
            value["job_details"]
        )
    if "source_language_code" in value:
        out["SourceLanguageCode"] = value["source_language_code"]
    if "target_language_codes" in value:
        import aws_sdk_translate.types.target_language_code_string_list

        out["TargetLanguageCodes"] = (
            aws_sdk_translate.types.target_language_code_string_list.serialize_aws_json_1_1(
                value["target_language_codes"]
            )
        )
    if "terminology_names" in value:
        import aws_sdk_translate.types.resource_name_list

        out["TerminologyNames"] = (
            aws_sdk_translate.types.resource_name_list.serialize_aws_json_1_1(
                value["terminology_names"]
            )
        )
    if "parallel_data_names" in value:
        import aws_sdk_translate.types.resource_name_list

        out["ParallelDataNames"] = (
            aws_sdk_translate.types.resource_name_list.serialize_aws_json_1_1(
                value["parallel_data_names"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "submitted_time" in value:
        import aws_sdk_translate.types.timestamp

        out["SubmittedTime"] = aws_sdk_translate.types.timestamp.serialize_aws_json_1_1(
            value["submitted_time"]
        )
    if "end_time" in value:
        import aws_sdk_translate.types.timestamp

        out["EndTime"] = aws_sdk_translate.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "input_data_config" in value:
        import aws_sdk_translate.types.input_data_config

        out["InputDataConfig"] = (
            aws_sdk_translate.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "output_data_config" in value:
        import aws_sdk_translate.types.output_data_config

        out["OutputDataConfig"] = (
            aws_sdk_translate.types.output_data_config.serialize_aws_json_1_1(
                value["output_data_config"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "settings" in value:
        import aws_sdk_translate.types.translation_settings

        out["Settings"] = (
            aws_sdk_translate.types.translation_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TextTranslationJobProperties:
    out: TextTranslationJobProperties = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "JobStatus" in data:
        import aws_sdk_translate.types.job_status

        out["job_status"] = aws_sdk_translate.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    if "JobDetails" in data:
        import aws_sdk_translate.types.job_details

        out["job_details"] = (
            aws_sdk_translate.types.job_details.deserialize_aws_json_1_1(
                data["JobDetails"]
            )
        )
    if "SourceLanguageCode" in data:
        out["source_language_code"] = data["SourceLanguageCode"]
    if "TargetLanguageCodes" in data:
        import aws_sdk_translate.types.target_language_code_string_list

        out["target_language_codes"] = (
            aws_sdk_translate.types.target_language_code_string_list.deserialize_aws_json_1_1(
                data["TargetLanguageCodes"]
            )
        )
    if "TerminologyNames" in data:
        import aws_sdk_translate.types.resource_name_list

        out["terminology_names"] = (
            aws_sdk_translate.types.resource_name_list.deserialize_aws_json_1_1(
                data["TerminologyNames"]
            )
        )
    if "ParallelDataNames" in data:
        import aws_sdk_translate.types.resource_name_list

        out["parallel_data_names"] = (
            aws_sdk_translate.types.resource_name_list.deserialize_aws_json_1_1(
                data["ParallelDataNames"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "SubmittedTime" in data:
        import aws_sdk_translate.types.timestamp

        out["submitted_time"] = (
            aws_sdk_translate.types.timestamp.deserialize_aws_json_1_1(
                data["SubmittedTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_translate.types.timestamp

        out["end_time"] = aws_sdk_translate.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "InputDataConfig" in data:
        import aws_sdk_translate.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_translate.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if "OutputDataConfig" in data:
        import aws_sdk_translate.types.output_data_config

        out["output_data_config"] = (
            aws_sdk_translate.types.output_data_config.deserialize_aws_json_1_1(
                data["OutputDataConfig"]
            )
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "Settings" in data:
        import aws_sdk_translate.types.translation_settings

        out["settings"] = (
            aws_sdk_translate.types.translation_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    return out
