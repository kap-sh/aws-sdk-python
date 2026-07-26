"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StopUploadJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name


class StopUploadJobRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain containing the upload job to stop. </p>"""
    job_id: "capo_customer_profiles.types.name.name"
    """<p>The unique identifier of the upload job to stop. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopUploadJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopUploadJobRequest:
    out: StopUploadJobRequest = {}  # type: ignore[typeddict-item]
    return out
