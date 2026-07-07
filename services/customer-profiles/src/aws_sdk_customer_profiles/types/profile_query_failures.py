"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileQueryFailures``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.get_segment_membership_message
    import aws_sdk_customer_profiles.types.get_segment_membership_status
    import aws_sdk_customer_profiles.types.profile_id


class ProfileQueryFailures(TypedDict, closed=True):
    profile_id: "aws_sdk_customer_profiles.types.profile_id.ProfileId"
    """<p>The profile id the failure belongs to.</p>"""
    message: "aws_sdk_customer_profiles.types.get_segment_membership_message.GetSegmentMembershipMessage"
    """<p>A message describing the failure.</p>"""
    status: NotRequired[
        "aws_sdk_customer_profiles.types.get_segment_membership_status.GetSegmentMembershipStatus"
    ]
    """<p>The status describing the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQueryFailures) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    out["Message"] = value["message"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> ProfileQueryFailures:
    out: ProfileQueryFailures = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    else:
        raise DeserializationError("ProfileQueryFailures.profile_id required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ProfileQueryFailures.message required")
    if "Status" in data:
        out["status"] = data["Status"]
    return out
