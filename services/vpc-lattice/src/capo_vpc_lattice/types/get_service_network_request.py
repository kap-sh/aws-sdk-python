"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetServiceNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_network_identifier


class GetServiceNetworkRequest(TypedDict, closed=True):
    service_network_identifier: (
        "capo_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
    )
    """<p>The ID or ARN of the service network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServiceNetworkRequest:
    out: GetServiceNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
