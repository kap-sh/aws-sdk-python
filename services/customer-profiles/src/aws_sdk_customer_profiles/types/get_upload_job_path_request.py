"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetUploadJobPathRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name


class GetUploadJobPathRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain containing the upload job. </p>"""
    job_id: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique identifier of the upload job to retrieve the upload path for. This is generated from the CreateUploadJob API. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUploadJobPathRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUploadJobPathRequest:
    out: GetUploadJobPathRequest = {}  # type: ignore[typeddict-item]
    return out
