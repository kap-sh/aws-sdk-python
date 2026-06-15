"""Generated from Smithy shape ``com.amazonaws.guardduty#GetMemberDetectorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.account_ids
    import aws_sdk_guardduty.types.detector_id


class GetMemberDetectorsRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The detector ID for the administrator account.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    account_ids: NotRequired["aws_sdk_guardduty.types.account_ids.AccountIds"]
    """<p>A list of member account IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemberDetectorsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_guardduty.types.account_ids

        out["accountIds"] = aws_sdk_guardduty.types.account_ids.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> GetMemberDetectorsRequest:
    out: GetMemberDetectorsRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_guardduty.types.account_ids

        out["account_ids"] = aws_sdk_guardduty.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    return out
