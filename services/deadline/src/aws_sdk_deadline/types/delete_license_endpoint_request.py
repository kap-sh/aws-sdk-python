"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteLicenseEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.license_endpoint_id


class DeleteLicenseEndpointRequest(TypedDict, closed=True):
    license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId"
    """<p>The license endpoint ID of the license endpoint to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLicenseEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLicenseEndpointRequest:
    out: DeleteLicenseEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
