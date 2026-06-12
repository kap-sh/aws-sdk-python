"""Generated from Smithy shape ``com.amazonaws.fis#GetTargetResourceTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.target_resource_type_id


class GetTargetResourceTypeRequest(TypedDict):
    resource_type: "aws_sdk_fis.types.target_resource_type_id.TargetResourceTypeId"
    """<p>The resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTargetResourceTypeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTargetResourceTypeRequest:
    out: GetTargetResourceTypeRequest = {}  # type: ignore[typeddict-item]
    return out
