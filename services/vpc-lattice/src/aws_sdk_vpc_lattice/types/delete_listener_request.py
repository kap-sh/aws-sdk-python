"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteListenerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.listener_identifier
    import aws_sdk_vpc_lattice.types.service_identifier


class DeleteListenerRequest(TypedDict):
    service_identifier: "aws_sdk_vpc_lattice.types.service_identifier.ServiceIdentifier"
    """<p>The ID or ARN of the service.</p>"""
    listener_identifier: (
        "aws_sdk_vpc_lattice.types.listener_identifier.ListenerIdentifier"
    )
    """<p>The ID or ARN of the listener.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteListenerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteListenerRequest:
    out: DeleteListenerRequest = {}  # type: ignore[typeddict-item]
    return out
