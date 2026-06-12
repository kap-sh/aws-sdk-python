"""Generated from Smithy shape ``com.amazonaws.batch#DeleteConsumableResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class DeleteConsumableResourceRequest(TypedDict):
    consumable_resource: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name or ARN of the consumable resource that will be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConsumableResourceRequest) -> dict:
    out: dict = {}
    if "consumable_resource" in value:
        out["consumableResource"] = value["consumable_resource"]
    return out


def deserialize_json(data: dict) -> DeleteConsumableResourceRequest:
    out: DeleteConsumableResourceRequest = {}  # type: ignore[typeddict-item]
    if "consumableResource" in data:
        out["consumable_resource"] = data["consumableResource"]
    return out
