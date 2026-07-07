"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_identifier


class GetServiceRequest(TypedDict, closed=True):
    service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServiceRequest:
    out: GetServiceRequest = {}  # type: ignore[typeddict-item]
    return out
