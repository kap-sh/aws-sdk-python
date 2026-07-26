"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IdentityResolutionJobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.identity_resolution_job

IdentityResolutionJobsList: TypeAlias = list[
    "capo_customer_profiles.types.identity_resolution_job.IdentityResolutionJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityResolutionJobsList) -> list:
    import capo_customer_profiles.types.identity_resolution_job

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.identity_resolution_job.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IdentityResolutionJobsList:
    import capo_customer_profiles.types.identity_resolution_job

    out: IdentityResolutionJobsList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.identity_resolution_job.deserialize_json(item)
        )
    return out
