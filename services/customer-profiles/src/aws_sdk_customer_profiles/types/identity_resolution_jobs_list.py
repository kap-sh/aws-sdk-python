"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IdentityResolutionJobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.identity_resolution_job

IdentityResolutionJobsList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.identity_resolution_job.IdentityResolutionJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityResolutionJobsList) -> list:
    import aws_sdk_customer_profiles.types.identity_resolution_job

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.identity_resolution_job.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IdentityResolutionJobsList:
    import aws_sdk_customer_profiles.types.identity_resolution_job

    out: IdentityResolutionJobsList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.identity_resolution_job.deserialize_json(
                item
            )
        )
    return out
