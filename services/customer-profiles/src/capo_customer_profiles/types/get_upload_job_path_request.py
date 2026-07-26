"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetUploadJobPathRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name


class GetUploadJobPathRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain containing the upload job. </p>"""
    job_id: "capo_customer_profiles.types.name.name"
    """<p>The unique identifier of the upload job to retrieve the upload path for. This is generated from the CreateUploadJob API. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUploadJobPathRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUploadJobPathRequest:
    out: GetUploadJobPathRequest = {}  # type: ignore[typeddict-item]
    return out
