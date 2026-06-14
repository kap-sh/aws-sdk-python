"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UpdateLookupTableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.arn
    import aws_sdk_cloudwatch_logs.types.kms_key_id
    import aws_sdk_cloudwatch_logs.types.lookup_table_description
    import aws_sdk_cloudwatch_logs.types.table_body


class UpdateLookupTableRequest(TypedDict):
    lookup_table_arn: "aws_sdk_cloudwatch_logs.types.arn.Arn"
    """<p>The ARN of the lookup table to update.</p>"""
    description: NotRequired[
        "aws_sdk_cloudwatch_logs.types.lookup_table_description.LookupTableDescription"
    ]
    """<p>An updated description of the lookup table.</p>"""
    table_body: "aws_sdk_cloudwatch_logs.types.table_body.TableBody"
    """<p>The new CSV content to replace the existing data. The first row must be a header row with column names. The content must use UTF-8 encoding and not exceed 10 MB.</p>"""
    kms_key_id: NotRequired["aws_sdk_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The ARN of the KMS key to use to encrypt the lookup table data. You can use this parameter to add, update, or remove the KMS key. To remove the KMS key and use an Amazon Web Services-owned key instead, specify an empty string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLookupTableRequest) -> dict:
    out: dict = {}
    out["lookupTableArn"] = value["lookup_table_arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["tableBody"] = value["table_body"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLookupTableRequest:
    out: UpdateLookupTableRequest = {}  # type: ignore[typeddict-item]
    if "lookupTableArn" in data:
        out["lookup_table_arn"] = data["lookupTableArn"]
    else:
        raise DeserializationError("UpdateLookupTableRequest.lookup_table_arn required")
    if "description" in data:
        out["description"] = data["description"]
    if "tableBody" in data:
        out["table_body"] = data["tableBody"]
    else:
        raise DeserializationError("UpdateLookupTableRequest.table_body required")
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
