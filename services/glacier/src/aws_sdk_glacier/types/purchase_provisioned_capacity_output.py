"""Generated from Smithy shape ``com.amazonaws.glacier#PurchaseProvisionedCapacityOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class PurchaseProvisionedCapacityOutput(TypedDict):
    capacity_id: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The ID that identifies the provisioned capacity unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseProvisionedCapacityOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PurchaseProvisionedCapacityOutput:
    out: PurchaseProvisionedCapacityOutput = {}  # type: ignore[typeddict-item]
    return out
