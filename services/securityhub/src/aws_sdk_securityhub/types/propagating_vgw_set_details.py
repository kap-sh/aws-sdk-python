"""Generated from Smithy shape ``com.amazonaws.securityhub#PropagatingVgwSetDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class PropagatingVgwSetDetails(TypedDict):
    gateway_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the virtual private gateway. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropagatingVgwSetDetails) -> dict:
    out: dict = {}
    if "gateway_id" in value:
        out["GatewayId"] = value["gateway_id"]
    return out


def deserialize_json(data: dict) -> PropagatingVgwSetDetails:
    out: PropagatingVgwSetDetails = {}  # type: ignore[typeddict-item]
    if "GatewayId" in data:
        out["gateway_id"] = data["GatewayId"]
    return out
