"""Generated from Smithy shape ``com.amazonaws.eks#CreateCapabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.capability


class CreateCapabilityResponse(TypedDict, closed=True):
    capability: NotRequired["capo_eks.types.capability.Capability"]
    """<p>An object containing information about the newly created capability, including its name, ARN, status, and configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCapabilityResponse) -> dict:
    out: dict = {}
    if "capability" in value:
        import capo_eks.types.capability

        out["capability"] = capo_eks.types.capability.serialize_json(
            value["capability"]
        )
    return out


def deserialize_json(data: dict) -> CreateCapabilityResponse:
    out: CreateCapabilityResponse = {}  # type: ignore[typeddict-item]
    if "capability" in data:
        import capo_eks.types.capability

        out["capability"] = capo_eks.types.capability.deserialize_json(
            data["capability"]
        )
    return out
