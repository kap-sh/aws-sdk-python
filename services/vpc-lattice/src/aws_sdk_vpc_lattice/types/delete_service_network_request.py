"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteServiceNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_network_identifier


class DeleteServiceNetworkRequest(TypedDict, closed=True):
    service_network_identifier: (
        "aws_sdk_vpc_lattice.types.service_network_identifier.ServiceNetworkIdentifier"
    )
    """<p>The ID or ARN of the service network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteServiceNetworkRequest:
    out: DeleteServiceNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
