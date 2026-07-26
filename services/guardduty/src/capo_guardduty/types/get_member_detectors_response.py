"""Generated from Smithy shape ``com.amazonaws.guardduty#GetMemberDetectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.member_data_source_configurations
    import capo_guardduty.types.unprocessed_accounts


class GetMemberDetectorsResponse(TypedDict, closed=True):
    member_data_source_configurations: NotRequired[
        "capo_guardduty.types.member_data_source_configurations.MemberDataSourceConfigurations"
    ]
    """<p>An object that describes which data sources are enabled for a member account.</p>"""
    unprocessed_accounts: NotRequired[
        "capo_guardduty.types.unprocessed_accounts.UnprocessedAccounts"
    ]
    """<p>A list of member account IDs that were unable to be processed along with an explanation for why they were not processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemberDetectorsResponse) -> dict:
    out: dict = {}
    if "member_data_source_configurations" in value:
        import capo_guardduty.types.member_data_source_configurations

        out["members"] = (
            capo_guardduty.types.member_data_source_configurations.serialize_json(
                value["member_data_source_configurations"]
            )
        )
    if "unprocessed_accounts" in value:
        import capo_guardduty.types.unprocessed_accounts

        out["unprocessedAccounts"] = (
            capo_guardduty.types.unprocessed_accounts.serialize_json(
                value["unprocessed_accounts"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMemberDetectorsResponse:
    out: GetMemberDetectorsResponse = {}  # type: ignore[typeddict-item]
    if "members" in data:
        import capo_guardduty.types.member_data_source_configurations

        out["member_data_source_configurations"] = (
            capo_guardduty.types.member_data_source_configurations.deserialize_json(
                data["members"]
            )
        )
    if "unprocessedAccounts" in data:
        import capo_guardduty.types.unprocessed_accounts

        out["unprocessed_accounts"] = (
            capo_guardduty.types.unprocessed_accounts.deserialize_json(
                data["unprocessedAccounts"]
            )
        )
    return out
