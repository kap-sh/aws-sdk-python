"""Generated from Smithy shape ``com.amazonaws.supplychain#GetInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.uuid


class GetInstanceRequest(TypedDict):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInstanceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInstanceRequest:
    out: GetInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
