"""Generated from Smithy shape ``com.amazonaws.guardduty#GetMembersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_ids
    import aws_sdk_guardduty.types.detector_id


class GetMembersRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The unique ID of the detector of the GuardDuty account whose members you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    account_ids: NotRequired["aws_sdk_guardduty.types.account_ids.AccountIds"]
    """<p>A list of account IDs of the GuardDuty member accounts that you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMembersRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_guardduty.types.account_ids

        out["accountIds"] = aws_sdk_guardduty.types.account_ids.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> GetMembersRequest:
    out: GetMembersRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_guardduty.types.account_ids

        out["account_ids"] = aws_sdk_guardduty.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    return out
