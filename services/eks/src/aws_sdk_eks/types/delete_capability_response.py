"""Generated from Smithy shape ``com.amazonaws.eks#DeleteCapabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.capability


class DeleteCapabilityResponse(TypedDict, closed=True):
    capability: NotRequired["aws_sdk_eks.types.capability.Capability"]
    """<p>An object containing information about the deleted capability, including its final status and configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCapabilityResponse) -> dict:
    out: dict = {}
    if "capability" in value:
        import aws_sdk_eks.types.capability

        out["capability"] = aws_sdk_eks.types.capability.serialize_json(
            value["capability"]
        )
    return out


def deserialize_json(data: dict) -> DeleteCapabilityResponse:
    out: DeleteCapabilityResponse = {}  # type: ignore[typeddict-item]
    if "capability" in data:
        import aws_sdk_eks.types.capability

        out["capability"] = aws_sdk_eks.types.capability.deserialize_json(
            data["capability"]
        )
    return out
