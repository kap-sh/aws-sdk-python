"""Generated from Smithy shape ``com.amazonaws.translate#ParallelDataProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_translate.types.description
    import aws_sdk_translate.types.encryption_key
    import aws_sdk_translate.types.language_code_string
    import aws_sdk_translate.types.language_code_string_list
    import aws_sdk_translate.types.long
    import aws_sdk_translate.types.parallel_data_arn
    import aws_sdk_translate.types.parallel_data_config
    import aws_sdk_translate.types.parallel_data_status
    import aws_sdk_translate.types.resource_name
    import aws_sdk_translate.types.timestamp
    import aws_sdk_translate.types.unbounded_length_string


class ParallelDataProperties(TypedDict):
    name: NotRequired["aws_sdk_translate.types.resource_name.ResourceName"]
    """<p>The custom name assigned to the parallel data resource.</p>"""
    arn: NotRequired["aws_sdk_translate.types.parallel_data_arn.ParallelDataArn"]
    """<p>The Amazon Resource Name (ARN) of the parallel data resource.</p>"""
    description: NotRequired["aws_sdk_translate.types.description.Description"]
    """<p>The description assigned to the parallel data resource.</p>"""
    status: NotRequired[
        "aws_sdk_translate.types.parallel_data_status.ParallelDataStatus"
    ]
    """<p>The status of the parallel data resource. When the parallel data is ready for you to use, the status is <code>ACTIVE</code>.</p>"""
    source_language_code: NotRequired[
        "aws_sdk_translate.types.language_code_string.LanguageCodeString"
    ]
    """<p>The source language of the translations in the parallel data file.</p>"""
    target_language_codes: NotRequired[
        "aws_sdk_translate.types.language_code_string_list.LanguageCodeStringList"
    ]
    """<p>The language codes for the target languages available in the parallel data file. All possible target languages are returned as an array.</p>"""
    parallel_data_config: NotRequired[
        "aws_sdk_translate.types.parallel_data_config.ParallelDataConfig"
    ]
    """<p>Specifies the format and S3 location of the parallel data input file.</p>"""
    message: NotRequired[
        "aws_sdk_translate.types.unbounded_length_string.UnboundedLengthString"
    ]
    """<p>Additional information from Amazon Translate about the parallel data resource. </p>"""
    imported_data_size: NotRequired["aws_sdk_translate.types.long.Long"]
    """<p>The number of UTF-8 characters that Amazon Translate imported from the parallel data input file. This number includes only the characters in your translation examples. It does not include characters that are used to format your file. For example, if you provided a Translation Memory Exchange (.tmx) file, this number does not include the tags.</p>"""
    imported_record_count: NotRequired["aws_sdk_translate.types.long.Long"]
    """<p>The number of records successfully imported from the parallel data input file.</p>"""
    failed_record_count: NotRequired["aws_sdk_translate.types.long.Long"]
    """<p>The number of records unsuccessfully imported from the parallel data input file.</p>"""
    skipped_record_count: NotRequired["aws_sdk_translate.types.long.Long"]
    """<p>The number of items in the input file that Amazon Translate skipped when you created or updated the parallel data resource. For example, Amazon Translate skips empty records, empty target texts, and empty lines.</p>"""
    encryption_key: NotRequired["aws_sdk_translate.types.encryption_key.EncryptionKey"]
    created_at: NotRequired["aws_sdk_translate.types.timestamp.Timestamp"]
    """<p>The time at which the parallel data resource was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_translate.types.timestamp.Timestamp"]
    """<p>The time at which the parallel data resource was last updated.</p>"""
    latest_update_attempt_status: NotRequired[
        "aws_sdk_translate.types.parallel_data_status.ParallelDataStatus"
    ]
    """<p>The status of the most recent update attempt for the parallel data resource.</p>"""
    latest_update_attempt_at: NotRequired["aws_sdk_translate.types.timestamp.Timestamp"]
    """<p>The time that the most recent update was attempted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelDataProperties) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_translate.types.parallel_data_status

        out["Status"] = (
            aws_sdk_translate.types.parallel_data_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "source_language_code" in value:
        out["SourceLanguageCode"] = value["source_language_code"]
    if "target_language_codes" in value:
        import aws_sdk_translate.types.language_code_string_list

        out["TargetLanguageCodes"] = (
            aws_sdk_translate.types.language_code_string_list.serialize_aws_json_1_1(
                value["target_language_codes"]
            )
        )
    if "parallel_data_config" in value:
        import aws_sdk_translate.types.parallel_data_config

        out["ParallelDataConfig"] = (
            aws_sdk_translate.types.parallel_data_config.serialize_aws_json_1_1(
                value["parallel_data_config"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "imported_data_size" in value:
        out["ImportedDataSize"] = value["imported_data_size"]
    if "imported_record_count" in value:
        out["ImportedRecordCount"] = value["imported_record_count"]
    if "failed_record_count" in value:
        out["FailedRecordCount"] = value["failed_record_count"]
    if "skipped_record_count" in value:
        out["SkippedRecordCount"] = value["skipped_record_count"]
    if "encryption_key" in value:
        import aws_sdk_translate.types.encryption_key

        out["EncryptionKey"] = (
            aws_sdk_translate.types.encryption_key.serialize_aws_json_1_1(
                value["encryption_key"]
            )
        )
    if "created_at" in value:
        import aws_sdk_translate.types.timestamp

        out["CreatedAt"] = aws_sdk_translate.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_translate.types.timestamp

        out["LastUpdatedAt"] = aws_sdk_translate.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_at"]
        )
    if "latest_update_attempt_status" in value:
        import aws_sdk_translate.types.parallel_data_status

        out["LatestUpdateAttemptStatus"] = (
            aws_sdk_translate.types.parallel_data_status.serialize_aws_json_1_1(
                value["latest_update_attempt_status"]
            )
        )
    if "latest_update_attempt_at" in value:
        import aws_sdk_translate.types.timestamp

        out["LatestUpdateAttemptAt"] = (
            aws_sdk_translate.types.timestamp.serialize_aws_json_1_1(
                value["latest_update_attempt_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParallelDataProperties:
    out: ParallelDataProperties = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_translate.types.parallel_data_status

        out["status"] = (
            aws_sdk_translate.types.parallel_data_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "SourceLanguageCode" in data:
        out["source_language_code"] = data["SourceLanguageCode"]
    if "TargetLanguageCodes" in data:
        import aws_sdk_translate.types.language_code_string_list

        out["target_language_codes"] = (
            aws_sdk_translate.types.language_code_string_list.deserialize_aws_json_1_1(
                data["TargetLanguageCodes"]
            )
        )
    if "ParallelDataConfig" in data:
        import aws_sdk_translate.types.parallel_data_config

        out["parallel_data_config"] = (
            aws_sdk_translate.types.parallel_data_config.deserialize_aws_json_1_1(
                data["ParallelDataConfig"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "ImportedDataSize" in data:
        out["imported_data_size"] = data["ImportedDataSize"]
    if "ImportedRecordCount" in data:
        out["imported_record_count"] = data["ImportedRecordCount"]
    if "FailedRecordCount" in data:
        out["failed_record_count"] = data["FailedRecordCount"]
    if "SkippedRecordCount" in data:
        out["skipped_record_count"] = data["SkippedRecordCount"]
    if "EncryptionKey" in data:
        import aws_sdk_translate.types.encryption_key

        out["encryption_key"] = (
            aws_sdk_translate.types.encryption_key.deserialize_aws_json_1_1(
                data["EncryptionKey"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_translate.types.timestamp

        out["created_at"] = aws_sdk_translate.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_translate.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_translate.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedAt"]
            )
        )
    if "LatestUpdateAttemptStatus" in data:
        import aws_sdk_translate.types.parallel_data_status

        out["latest_update_attempt_status"] = (
            aws_sdk_translate.types.parallel_data_status.deserialize_aws_json_1_1(
                data["LatestUpdateAttemptStatus"]
            )
        )
    if "LatestUpdateAttemptAt" in data:
        import aws_sdk_translate.types.timestamp

        out["latest_update_attempt_at"] = (
            aws_sdk_translate.types.timestamp.deserialize_aws_json_1_1(
                data["LatestUpdateAttemptAt"]
            )
        )
    return out
