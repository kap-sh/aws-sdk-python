"""Generated from Smithy shape ``com.amazonaws.deadline#CreateLicenseEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.license_endpoint_id


class CreateLicenseEndpointResponse(TypedDict):
    license_endpoint_id: "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId"
    """<p>The license endpoint ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLicenseEndpointResponse) -> dict:
    out: dict = {}
    out["licenseEndpointId"] = value["license_endpoint_id"]
    return out


def deserialize_json(data: dict) -> CreateLicenseEndpointResponse:
    out: CreateLicenseEndpointResponse = {}  # type: ignore[typeddict-item]
    if "licenseEndpointId" in data:
        out["license_endpoint_id"] = data["licenseEndpointId"]
    else:
        raise DeserializationError(
            "CreateLicenseEndpointResponse.license_endpoint_id required"
        )
    return out
