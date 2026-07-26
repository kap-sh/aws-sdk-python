"""Generated from Smithy shape ``com.amazonaws.fis#GetTargetResourceTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fis.types.target_resource_type_id


class GetTargetResourceTypeRequest(TypedDict, closed=True):
    resource_type: "capo_fis.types.target_resource_type_id.TargetResourceTypeId"
    """<p>The resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTargetResourceTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTargetResourceTypeRequest:
    out: GetTargetResourceTypeRequest = {}  # type: ignore[typeddict-item]
    return out
