"""Generated from Smithy shape ``com.amazonaws.datazone#UserProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.user_profile_details
    import capo_datazone.types.user_profile_id
    import capo_datazone.types.user_profile_status
    import capo_datazone.types.user_profile_type


class UserProfileSummary(TypedDict, closed=True):
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The ID of the Amazon DataZone domain of the user profile.</p>"""
    id: NotRequired["capo_datazone.types.user_profile_id.UserProfileId"]
    """<p>The ID of the user profile.</p>"""
    type: NotRequired["capo_datazone.types.user_profile_type.UserProfileType"]
    """<p>The type of the user profile.</p>"""
    status: NotRequired["capo_datazone.types.user_profile_status.UserProfileStatus"]
    """<p>The status of the user profile.</p>"""
    details: NotRequired["capo_datazone.types.user_profile_details.UserProfileDetails"]
    """<p>The details of the user profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserProfileSummary) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import capo_datazone.types.user_profile_type

        out["type"] = capo_datazone.types.user_profile_type.serialize_json(
            value["type"]
        )
    if "status" in value:
        import capo_datazone.types.user_profile_status

        out["status"] = capo_datazone.types.user_profile_status.serialize_json(
            value["status"]
        )
    if "details" in value:
        import capo_datazone.types.user_profile_details

        out["details"] = capo_datazone.types.user_profile_details.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> UserProfileSummary:
    out: UserProfileSummary = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        import capo_datazone.types.user_profile_type

        out["type"] = capo_datazone.types.user_profile_type.deserialize_json(
            data["type"]
        )
    if "status" in data:
        import capo_datazone.types.user_profile_status

        out["status"] = capo_datazone.types.user_profile_status.deserialize_json(
            data["status"]
        )
    if "details" in data:
        import capo_datazone.types.user_profile_details

        out["details"] = capo_datazone.types.user_profile_details.deserialize_json(
            data["details"]
        )
    return out
