"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSegmentMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.profile_ids


class GetSegmentMembershipRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    segment_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The Id of the wanted segment. Needs to be a valid, and existing segment Id.</p>"""
    profile_ids: "capo_customer_profiles.types.profile_ids.ProfileIds"
    """<p>The list of profile IDs to query for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentMembershipRequest) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.profile_ids

    out["ProfileIds"] = capo_customer_profiles.types.profile_ids.serialize_json(
        value["profile_ids"]
    )
    return out


def deserialize_json(data: dict) -> GetSegmentMembershipRequest:
    out: GetSegmentMembershipRequest = {}  # type: ignore[typeddict-item]
    if "ProfileIds" in data:
        import capo_customer_profiles.types.profile_ids

        out["profile_ids"] = capo_customer_profiles.types.profile_ids.deserialize_json(
            data["ProfileIds"]
        )
    else:
        raise DeserializationError("GetSegmentMembershipRequest.profile_ids required")
    return out
