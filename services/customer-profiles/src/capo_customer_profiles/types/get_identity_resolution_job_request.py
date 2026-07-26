"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetIdentityResolutionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.uuid


class GetIdentityResolutionJobRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    job_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of the Identity Resolution Job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdentityResolutionJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIdentityResolutionJobRequest:
    out: GetIdentityResolutionJobRequest = {}  # type: ignore[typeddict-item]
    return out
