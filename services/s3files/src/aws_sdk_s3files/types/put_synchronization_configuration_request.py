"""Generated from Smithy shape ``com.amazonaws.s3files#PutSynchronizationConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3files.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3files.types.expiration_data_rule_list
    import aws_sdk_s3files.types.file_system_id
    import aws_sdk_s3files.types.import_data_rule_list


class PutSynchronizationConfigurationRequest(TypedDict):
    file_system_id: "aws_sdk_s3files.types.file_system_id.FileSystemId"
    """<p>The ID or Amazon Resource Name (ARN) of the S3 File System to configure synchronization for.</p>"""
    latest_version_number: NotRequired["int"]
    """<p>The version number of the current synchronization configuration. Omit this value when creating a synchronization configuration for the first time. For subsequent updates, provide this value for optimistic concurrency control. If the version number does not match the current configuration, the request fails with a <code>ConflictException</code>.</p>"""
    import_data_rules: "aws_sdk_s3files.types.import_data_rule_list.ImportDataRuleList"
    """<p>An array of import data rules that control how data is imported from S3 into the file system.</p>"""
    expiration_data_rules: (
        "aws_sdk_s3files.types.expiration_data_rule_list.ExpirationDataRuleList"
    )
    """<p>An array of expiration data rules that control when cached data expires from the file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSynchronizationConfigurationRequest) -> dict:
    out: dict = {}
    if "latest_version_number" in value:
        out["latestVersionNumber"] = value["latest_version_number"]
    import aws_sdk_s3files.types.import_data_rule_list

    out["importDataRules"] = aws_sdk_s3files.types.import_data_rule_list.serialize_json(
        value["import_data_rules"]
    )
    import aws_sdk_s3files.types.expiration_data_rule_list

    out["expirationDataRules"] = (
        aws_sdk_s3files.types.expiration_data_rule_list.serialize_json(
            value["expiration_data_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutSynchronizationConfigurationRequest:
    out: PutSynchronizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "latestVersionNumber" in data:
        out["latest_version_number"] = data["latestVersionNumber"]
    if "importDataRules" in data:
        import aws_sdk_s3files.types.import_data_rule_list

        out["import_data_rules"] = (
            aws_sdk_s3files.types.import_data_rule_list.deserialize_json(
                data["importDataRules"]
            )
        )
    else:
        raise DeserializationError(
            "PutSynchronizationConfigurationRequest.import_data_rules required"
        )
    if "expirationDataRules" in data:
        import aws_sdk_s3files.types.expiration_data_rule_list

        out["expiration_data_rules"] = (
            aws_sdk_s3files.types.expiration_data_rule_list.deserialize_json(
                data["expirationDataRules"]
            )
        )
    else:
        raise DeserializationError(
            "PutSynchronizationConfigurationRequest.expiration_data_rules required"
        )
    return out
