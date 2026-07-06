"""Generated from Smithy shape ``com.amazonaws.batch#ConsumableResourceRequirement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.long
    import aws_sdk_batch.types.string


class ConsumableResourceRequirement(TypedDict, closed=True):
    consumable_resource: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name or ARN of the consumable resource.</p>"""
    quantity: NotRequired["aws_sdk_batch.types.long.Long"]
    """<p>The quantity of the consumable resource that is needed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsumableResourceRequirement) -> dict:
    out: dict = {}
    if "consumable_resource" in value:
        out["consumableResource"] = value["consumable_resource"]
    if "quantity" in value:
        out["quantity"] = value["quantity"]
    return out


def deserialize_json(data: dict) -> ConsumableResourceRequirement:
    out: ConsumableResourceRequirement = {}  # type: ignore[typeddict-item]
    if "consumableResource" in data:
        out["consumable_resource"] = data["consumableResource"]
    if "quantity" in data:
        out["quantity"] = data["quantity"]
    return out
