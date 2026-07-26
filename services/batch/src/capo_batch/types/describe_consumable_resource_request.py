"""Generated from Smithy shape ``com.amazonaws.batch#DescribeConsumableResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string


class DescribeConsumableResourceRequest(TypedDict, closed=True):
    consumable_resource: NotRequired["capo_batch.types.string.String"]
    """<p>The name or ARN of the consumable resource whose description will be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConsumableResourceRequest) -> dict:
    out: dict = {}
    if "consumable_resource" in value:
        out["consumableResource"] = value["consumable_resource"]
    return out


def deserialize_json(data: dict) -> DescribeConsumableResourceRequest:
    out: DescribeConsumableResourceRequest = {}  # type: ignore[typeddict-item]
    if "consumableResource" in data:
        out["consumable_resource"] = data["consumableResource"]
    return out
