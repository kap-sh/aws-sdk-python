"""Generated from Smithy shape ``com.amazonaws.sesv2#GetDedicatedIpRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.ip


class GetDedicatedIpRequest(TypedDict, closed=True):
    ip: "aws_sdk_sesv2.types.ip.Ip"
    """<p>The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that's assocaited with your Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDedicatedIpRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDedicatedIpRequest:
    out: GetDedicatedIpRequest = {}  # type: ignore[typeddict-item]
    return out
