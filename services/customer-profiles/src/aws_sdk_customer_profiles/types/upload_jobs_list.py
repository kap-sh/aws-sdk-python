"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UploadJobsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.upload_job_item

UploadJobsList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.upload_job_item.UploadJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: UploadJobsList) -> list:
    import aws_sdk_customer_profiles.types.upload_job_item

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.upload_job_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> UploadJobsList:
    import aws_sdk_customer_profiles.types.upload_job_item

    out: UploadJobsList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.upload_job_item.deserialize_json(item)
        )
    return out
