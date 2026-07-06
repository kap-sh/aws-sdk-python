"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentsSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.attachment_identifier
    import aws_sdk_ssm.types.attachments_source_key
    import aws_sdk_ssm.types.attachments_source_values


class AttachmentsSource(TypedDict, closed=True):
    key: NotRequired["aws_sdk_ssm.types.attachments_source_key.AttachmentsSourceKey"]
    """<p>The key of a key-value pair that identifies the location of an attachment to a document.</p>"""
    values: NotRequired[
        "aws_sdk_ssm.types.attachments_source_values.AttachmentsSourceValues"
    ]
    r"""<p>The value of a key-value pair that identifies the location of an attachment to a document. The format for <b>Value</b> depends on the type of key you specify.</p> <ul> <li> <p>For the key <i>SourceUrl</i>, the value is an S3 bucket location. For example:</p> <p> <code>\"Values\": [ \"s3://amzn-s3-demo-bucket/my-prefix\" ]</code> </p> </li> <li> <p>For the key <i>S3FileUrl</i>, the value is a file in an S3 bucket. For example:</p> <p> <code>\"Values\": [ \"s3://amzn-s3-demo-bucket/my-prefix/my-file.py\" ]</code> </p> </li> <li> <p>For the key <i>AttachmentReference</i>, the value is constructed from the name of another SSM document in your account, a version number of that document, and a file attached to that document version that you want to reuse. For example:</p> <p> <code>\"Values\": [ \"MyOtherDocument/3/my-other-file.py\" ]</code> </p> <p>However, if the SSM document is shared with you from another account, the full SSM document ARN must be specified instead of the document name only. For example:</p> <p> <code>\"Values\": [ \"arn:aws:ssm:us-east-2:111122223333:document/OtherAccountDocument/3/their-file.py\" ]</code> </p> </li> </ul>"""
    name: NotRequired["aws_sdk_ssm.types.attachment_identifier.AttachmentIdentifier"]
    """<p>The name of the document attachment file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentsSource) -> dict:
    out: dict = {}
    if "key" in value:
        import aws_sdk_ssm.types.attachments_source_key

        out["Key"] = aws_sdk_ssm.types.attachments_source_key.serialize_aws_json_1_1(
            value["key"]
        )
    if "values" in value:
        import aws_sdk_ssm.types.attachments_source_values

        out["Values"] = (
            aws_sdk_ssm.types.attachments_source_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentsSource:
    out: AttachmentsSource = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_ssm.types.attachments_source_key

        out["key"] = aws_sdk_ssm.types.attachments_source_key.deserialize_aws_json_1_1(
            data["Key"]
        )
    if "Values" in data:
        import aws_sdk_ssm.types.attachments_source_values

        out["values"] = (
            aws_sdk_ssm.types.attachments_source_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    return out
