"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateLookupTableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.kms_key_id
    import aws_sdk_cloudwatch_logs.types.lookup_table_description
    import aws_sdk_cloudwatch_logs.types.lookup_table_name
    import aws_sdk_cloudwatch_logs.types.table_body
    import aws_sdk_cloudwatch_logs.types.tags


class CreateLookupTableRequest(TypedDict):
    lookup_table_name: "aws_sdk_cloudwatch_logs.types.lookup_table_name.LookupTableName"
    """<p>The name of the lookup table. The name must be unique within your account and Region. The name can contain only alphanumeric characters and underscores, and can be up to 256 characters long.</p>"""
    description: NotRequired[
        "aws_sdk_cloudwatch_logs.types.lookup_table_description.LookupTableDescription"
    ]
    """<p>A description of the lookup table. The description can be up to 1024 characters long.</p>"""
    table_body: "aws_sdk_cloudwatch_logs.types.table_body.TableBody"
    """<p>The CSV content of the lookup table. The first row must be a header row with column names. The content must use UTF-8 encoding and not exceed 10 MB.</p>"""
    kms_key_id: NotRequired["aws_sdk_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The ARN of the KMS key to use to encrypt the lookup table data. If you don't specify a key, the data is encrypted with an Amazon Web Services-owned key.</p>"""
    tags: NotRequired["aws_sdk_cloudwatch_logs.types.tags.Tags"]
    """<p>A list of key-value pairs to associate with the lookup table. You can associate as many as 50 tags with a lookup table. Tags can help you organize and categorize your resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLookupTableRequest) -> dict:
    out: dict = {}
    out["lookupTableName"] = value["lookup_table_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["tableBody"] = value["table_body"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLookupTableRequest:
    out: CreateLookupTableRequest = {}  # type: ignore[typeddict-item]
    if "lookupTableName" in data:
        out["lookup_table_name"] = data["lookupTableName"]
    else:
        raise DeserializationError(
            "CreateLookupTableRequest.lookup_table_name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tableBody" in data:
        out["table_body"] = data["tableBody"]
    else:
        raise DeserializationError("CreateLookupTableRequest.table_body required")
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "tags" in data:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
