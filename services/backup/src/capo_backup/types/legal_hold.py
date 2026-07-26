"""Generated from Smithy shape ``com.amazonaws.backup#LegalHold``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.legal_hold_status
    import capo_backup.types.string
    import capo_backup.types.timestamp


class LegalHold(TypedDict, closed=True):
    title: NotRequired["capo_backup.types.string.string"]
    """<p>The title of a legal hold.</p>"""
    status: NotRequired["capo_backup.types.legal_hold_status.LegalHoldStatus"]
    """<p>The status of the legal hold.</p>"""
    description: NotRequired["capo_backup.types.string.string"]
    """<p>The description of a legal hold.</p>"""
    legal_hold_id: NotRequired["capo_backup.types.string.string"]
    """<p>The ID of the legal hold.</p>"""
    legal_hold_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the legal hold; for example, <code>arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45</code>.</p>"""
    creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The time when the legal hold was created.</p>"""
    cancellation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>The time when the legal hold was cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LegalHold) -> dict:
    out: dict = {}
    if "title" in value:
        out["Title"] = value["title"]
    if "status" in value:
        import capo_backup.types.legal_hold_status

        out["Status"] = capo_backup.types.legal_hold_status.serialize_json(
            value["status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "legal_hold_id" in value:
        out["LegalHoldId"] = value["legal_hold_id"]
    if "legal_hold_arn" in value:
        out["LegalHoldArn"] = value["legal_hold_arn"]
    if "creation_date" in value:
        import capo_backup.types.timestamp

        out["CreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "cancellation_date" in value:
        import capo_backup.types.timestamp

        out["CancellationDate"] = capo_backup.types.timestamp.serialize_json(
            value["cancellation_date"]
        )
    return out


def deserialize_json(data: dict) -> LegalHold:
    out: LegalHold = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Status" in data:
        import capo_backup.types.legal_hold_status

        out["status"] = capo_backup.types.legal_hold_status.deserialize_json(
            data["Status"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "LegalHoldId" in data:
        out["legal_hold_id"] = data["LegalHoldId"]
    if "LegalHoldArn" in data:
        out["legal_hold_arn"] = data["LegalHoldArn"]
    if "CreationDate" in data:
        import capo_backup.types.timestamp

        out["creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "CancellationDate" in data:
        import capo_backup.types.timestamp

        out["cancellation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CancellationDate"]
        )
    return out
