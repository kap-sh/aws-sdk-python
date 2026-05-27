"""Generated from Smithy shape ``com.amazonaws.eks#CreateCapabilityResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.capability


class CreateCapabilityResponse(TypedDict):
    capability: NotRequired["aws_sdk_eks.types.capability.Capability"]
    """<p>An object containing information about the newly created capability, including its name, ARN, status, and configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCapabilityResponse) -> dict:
    out: dict = {}
    if "capability" in value:
        import aws_sdk_eks.types.capability

        out["capability"] = aws_sdk_eks.types.capability.serialize_json(
            value["capability"]
        )
    return out


def deserialize_json(data: dict) -> CreateCapabilityResponse:
    out: CreateCapabilityResponse = {}  # type: ignore[typeddict-item]
    if "capability" in data:
        import aws_sdk_eks.types.capability

        out["capability"] = aws_sdk_eks.types.capability.deserialize_json(
            data["capability"]
        )
    return out
