"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListProfileHistoryRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.profile_history_records
    import capo_customer_profiles.types.token


class ListProfileHistoryRecordsResponse(TypedDict, closed=True):
    profile_history_records: NotRequired[
        "capo_customer_profiles.types.profile_history_records.ProfileHistoryRecords"
    ]
    """<p>The list of profile history records.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileHistoryRecordsResponse) -> dict:
    out: dict = {}
    if "profile_history_records" in value:
        import capo_customer_profiles.types.profile_history_records

        out["ProfileHistoryRecords"] = (
            capo_customer_profiles.types.profile_history_records.serialize_json(
                value["profile_history_records"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfileHistoryRecordsResponse:
    out: ListProfileHistoryRecordsResponse = {}  # type: ignore[typeddict-item]
    if "ProfileHistoryRecords" in data:
        import capo_customer_profiles.types.profile_history_records

        out["profile_history_records"] = (
            capo_customer_profiles.types.profile_history_records.deserialize_json(
                data["ProfileHistoryRecords"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
