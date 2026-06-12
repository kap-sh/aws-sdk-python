"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetUploadJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.uuid


class GetUploadJobRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain containing the upload job. </p>"""
    job_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of the upload job to retrieve. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUploadJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUploadJobRequest:
    out: GetUploadJobRequest = {}  # type: ignore[typeddict-item]
    return out
