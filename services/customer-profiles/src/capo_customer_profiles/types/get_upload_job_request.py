"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetUploadJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.uuid


class GetUploadJobRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain containing the upload job. </p>"""
    job_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of the upload job to retrieve. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUploadJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUploadJobRequest:
    out: GetUploadJobRequest = {}  # type: ignore[typeddict-item]
    return out
