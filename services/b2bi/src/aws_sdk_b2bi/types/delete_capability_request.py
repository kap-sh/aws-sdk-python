"""Generated from Smithy shape ``com.amazonaws.b2bi#DeleteCapabilityRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.capability_id


class DeleteCapabilityRequest(TypedDict):
    capability_id: "aws_sdk_b2bi.types.capability_id.CapabilityId"
    """<p>Specifies a system-assigned unique identifier for the capability.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteCapabilityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteCapabilityRequest:
    out: DeleteCapabilityRequest = {}  # type: ignore[typeddict-item]
    return out
