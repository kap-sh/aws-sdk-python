"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetListenerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.listener_identifier
    import capo_vpc_lattice.types.service_identifier


class GetListenerRequest(TypedDict, closed=True):
    service_identifier: "capo_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    listener_identifier: "capo_vpc_lattice.types.listener_identifier.ListenerIdentifier"
    """<p>The ID or ARN of the listener.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetListenerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetListenerRequest:
    out: GetListenerRequest = {}  # type: ignore[typeddict-item]
    return out
