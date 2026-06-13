"""Generated from Smithy shape ``com.amazonaws.backup#GetLegalHoldOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.legal_hold_status
    import aws_sdk_backup.types.recovery_point_selection
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.timestamp


class GetLegalHoldOutput(TypedDict):
    title: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The title of the legal hold.</p>"""
    status: NotRequired["aws_sdk_backup.types.legal_hold_status.LegalHoldStatus"]
    """<p>The status of the legal hold.</p>"""
    description: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The description of the legal hold.</p>"""
    cancel_description: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The reason for removing the legal hold.</p>"""
    legal_hold_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The ID of the legal hold.</p>"""
    legal_hold_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>The framework ARN for the specified legal hold. The format of the ARN depends on the resource type.</p>"""
    creation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The time when the legal hold was created.</p>"""
    cancellation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The time when the legal hold was cancelled.</p>"""
    retain_record_until: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time until which the legal hold record is retained.</p>"""
    recovery_point_selection: NotRequired[
        "aws_sdk_backup.types.recovery_point_selection.RecoveryPointSelection"
    ]
    """<p>The criteria to assign a set of resources, such as resource types or backup vaults.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLegalHoldOutput) -> dict:
    out: dict = {}
    if "title" in value:
        out["Title"] = value["title"]
    if "status" in value:
        import aws_sdk_backup.types.legal_hold_status

        out["Status"] = aws_sdk_backup.types.legal_hold_status.serialize_json(
            value["status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "cancel_description" in value:
        out["CancelDescription"] = value["cancel_description"]
    if "legal_hold_id" in value:
        out["LegalHoldId"] = value["legal_hold_id"]
    if "legal_hold_arn" in value:
        out["LegalHoldArn"] = value["legal_hold_arn"]
    if "creation_date" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "cancellation_date" in value:
        import aws_sdk_backup.types.timestamp

        out["CancellationDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["cancellation_date"]
        )
    if "retain_record_until" in value:
        import aws_sdk_backup.types.timestamp

        out["RetainRecordUntil"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["retain_record_until"]
        )
    if "recovery_point_selection" in value:
        import aws_sdk_backup.types.recovery_point_selection

        out["RecoveryPointSelection"] = (
            aws_sdk_backup.types.recovery_point_selection.serialize_json(
                value["recovery_point_selection"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLegalHoldOutput:
    out: GetLegalHoldOutput = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Status" in data:
        import aws_sdk_backup.types.legal_hold_status

        out["status"] = aws_sdk_backup.types.legal_hold_status.deserialize_json(
            data["Status"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "CancelDescription" in data:
        out["cancel_description"] = data["CancelDescription"]
    if "LegalHoldId" in data:
        out["legal_hold_id"] = data["LegalHoldId"]
    if "LegalHoldArn" in data:
        out["legal_hold_arn"] = data["LegalHoldArn"]
    if "CreationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "CancellationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["cancellation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CancellationDate"]
        )
    if "RetainRecordUntil" in data:
        import aws_sdk_backup.types.timestamp

        out["retain_record_until"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["RetainRecordUntil"]
        )
    if "RecoveryPointSelection" in data:
        import aws_sdk_backup.types.recovery_point_selection

        out["recovery_point_selection"] = (
            aws_sdk_backup.types.recovery_point_selection.deserialize_json(
                data["RecoveryPointSelection"]
            )
        )
    return out
