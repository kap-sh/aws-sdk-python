"""Generated from Smithy shape ``com.amazonaws.guardduty#DisassociateMembersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_ids
    import aws_sdk_guardduty.types.detector_id


class DisassociateMembersRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector of the GuardDuty account whose members you want to disassociate from the administrator account.</p>"""
    account_ids: NotRequired["aws_sdk_guardduty.types.account_ids.AccountIds"]
    """<p>A list of account IDs of the GuardDuty member accounts that you want to disassociate from the administrator account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMembersRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_guardduty.types.account_ids

        out["accountIds"] = aws_sdk_guardduty.types.account_ids.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> DisassociateMembersRequest:
    out: DisassociateMembersRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_guardduty.types.account_ids

        out["account_ids"] = aws_sdk_guardduty.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    return out
