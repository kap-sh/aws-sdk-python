"""Generated from Smithy shape ``com.amazonaws.deadline#GetLicenseEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.license_endpoint_id


class GetLicenseEndpointRequest(TypedDict):
    license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId"
    """<p>The license endpoint ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLicenseEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLicenseEndpointRequest:
    out: GetLicenseEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
