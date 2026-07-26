"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_identifier


class DeleteServiceRequest(TypedDict, closed=True):
    service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteServiceRequest:
    out: DeleteServiceRequest = {}  # type: ignore[typeddict-item]
    return out
