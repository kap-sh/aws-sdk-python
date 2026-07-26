"""Generated from Smithy shape ``com.amazonaws.eks#DescribeCapabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.capability


class DescribeCapabilityResponse(TypedDict, closed=True):
    capability: NotRequired["capo_eks.types.capability.Capability"]
    """<p>An object containing detailed information about the capability, including its name, ARN, type, status, version, configuration, health status, and timestamps for when it was created and last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCapabilityResponse) -> dict:
    out: dict = {}
    if "capability" in value:
        import capo_eks.types.capability

        out["capability"] = capo_eks.types.capability.serialize_json(
            value["capability"]
        )
    return out


def deserialize_json(data: dict) -> DescribeCapabilityResponse:
    out: DescribeCapabilityResponse = {}  # type: ignore[typeddict-item]
    if "capability" in data:
        import capo_eks.types.capability

        out["capability"] = capo_eks.types.capability.deserialize_json(
            data["capability"]
        )
    return out
