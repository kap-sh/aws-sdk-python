"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetProfileHistoryRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.uuid


class GetProfileHistoryRecordRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain for which to return a profile history record.</p>"""
    profile_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of the profile for which to return a history record.</p>"""
    id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of the profile history record to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileHistoryRecordRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProfileHistoryRecordRequest:
    out: GetProfileHistoryRecordRequest = {}  # type: ignore[typeddict-item]
    return out
