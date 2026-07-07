"""Generated from Smithy shape ``com.amazonaws.opensearch#DeregisterCapabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.capability_status


class DeregisterCapabilityResponse(TypedDict, closed=True):
    status: NotRequired["aws_sdk_opensearch.types.capability_status.CapabilityStatus"]
    """<p>The status of the deregistration operation. Returns <code>deleting</code> when the capability is being removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterCapabilityResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_opensearch.types.capability_status

        out["status"] = aws_sdk_opensearch.types.capability_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> DeregisterCapabilityResponse:
    out: DeregisterCapabilityResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_opensearch.types.capability_status

        out["status"] = aws_sdk_opensearch.types.capability_status.deserialize_json(
            data["status"]
        )
    return out
