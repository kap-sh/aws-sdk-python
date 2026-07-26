"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UploadJobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.upload_job_item

UploadJobsList: TypeAlias = list[
    "capo_customer_profiles.types.upload_job_item.UploadJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: UploadJobsList) -> list:
    import capo_customer_profiles.types.upload_job_item

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.upload_job_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> UploadJobsList:
    import capo_customer_profiles.types.upload_job_item

    out: UploadJobsList = []
    for item in data:
        out.append(capo_customer_profiles.types.upload_job_item.deserialize_json(item))
    return out
