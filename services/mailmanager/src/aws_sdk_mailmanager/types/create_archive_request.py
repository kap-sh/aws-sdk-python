"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateArchiveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archive_name_string
    import aws_sdk_mailmanager.types.archive_retention
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.kms_key_arn
    import aws_sdk_mailmanager.types.tag_list


class CreateArchiveRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token Amazon SES uses to recognize retries of this request.</p>"""
    archive_name: "aws_sdk_mailmanager.types.archive_name_string.ArchiveNameString"
    """<p>A unique name for the new archive.</p>"""
    retention: NotRequired[
        "aws_sdk_mailmanager.types.archive_retention.ArchiveRetention"
    ]
    """<p>The period for retaining emails in the archive before automatic deletion.</p>"""
    kms_key_arn: NotRequired["aws_sdk_mailmanager.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key for encrypting emails in the archive.</p>"""
    tags: NotRequired["aws_sdk_mailmanager.types.tag_list.TagList"]
    r"""<p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateArchiveRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ArchiveName"] = value["archive_name"]
    if "retention" in value:
        import aws_sdk_mailmanager.types.archive_retention

        out["Retention"] = (
            aws_sdk_mailmanager.types.archive_retention.serialize_aws_json_1_0(
                value["retention"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import aws_sdk_mailmanager.types.tag_list

        out["Tags"] = aws_sdk_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateArchiveRequest:
    out: CreateArchiveRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ArchiveName" in data:
        out["archive_name"] = data["ArchiveName"]
    else:
        raise DeserializationError("CreateArchiveRequest.archive_name required")
    if "Retention" in data:
        import aws_sdk_mailmanager.types.archive_retention

        out["retention"] = (
            aws_sdk_mailmanager.types.archive_retention.deserialize_aws_json_1_0(
                data["Retention"]
            )
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "Tags" in data:
        import aws_sdk_mailmanager.types.tag_list

        out["tags"] = aws_sdk_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
