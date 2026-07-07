"""Generated from Smithy shape ``com.amazonaws.eventbridge#UpdateArchiveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.archive_description
    import aws_sdk_eventbridge.types.archive_name
    import aws_sdk_eventbridge.types.event_pattern
    import aws_sdk_eventbridge.types.kms_key_identifier
    import aws_sdk_eventbridge.types.retention_days


class UpdateArchiveRequest(TypedDict, closed=True):
    archive_name: "aws_sdk_eventbridge.types.archive_name.ArchiveName"
    """<p>The name of the archive to update.</p>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.archive_description.ArchiveDescription"
    ]
    """<p>The description for the archive.</p>"""
    event_pattern: NotRequired["aws_sdk_eventbridge.types.event_pattern.EventPattern"]
    """<p>The event pattern to use to filter events sent to the archive.</p>"""
    retention_days: NotRequired[
        "aws_sdk_eventbridge.types.retention_days.RetentionDays"
    ]
    """<p>The number of days to retain events in the archive.</p>"""
    kms_key_identifier: NotRequired[
        "aws_sdk_eventbridge.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    r"""<p>The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt this archive. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.</p> <p>If you do not specify a customer managed key identifier, EventBridge uses an Amazon Web Services owned key to encrypt the archive.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html\">Identify and view keys</a> in the <i>Key Management Service Developer Guide</i>. </p> <important> <p>If you have specified that EventBridge use a customer managed key for encrypting the source event bus, we strongly recommend you also specify a customer managed key for any archives for the event bus as well. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-archives.html\">Encrypting archives</a> in the <i>Amazon EventBridge User Guide</i>.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateArchiveRequest) -> dict:
    out: dict = {}
    out["ArchiveName"] = value["archive_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "event_pattern" in value:
        out["EventPattern"] = value["event_pattern"]
    if "retention_days" in value:
        out["RetentionDays"] = value["retention_days"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateArchiveRequest:
    out: UpdateArchiveRequest = {}  # type: ignore[typeddict-item]
    if "ArchiveName" in data:
        out["archive_name"] = data["ArchiveName"]
    else:
        raise DeserializationError("UpdateArchiveRequest.archive_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "EventPattern" in data:
        out["event_pattern"] = data["EventPattern"]
    if "RetentionDays" in data:
        out["retention_days"] = data["RetentionDays"]
    if "KmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out
