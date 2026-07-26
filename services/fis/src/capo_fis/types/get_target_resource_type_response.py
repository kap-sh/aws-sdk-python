"""Generated from Smithy shape ``com.amazonaws.fis#GetTargetResourceTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.target_resource_type


class GetTargetResourceTypeResponse(TypedDict, closed=True):
    target_resource_type: NotRequired[
        "capo_fis.types.target_resource_type.TargetResourceType"
    ]
    """<p>Information about the resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTargetResourceTypeResponse) -> dict:
    out: dict = {}
    if "target_resource_type" in value:
        import capo_fis.types.target_resource_type

        out["targetResourceType"] = capo_fis.types.target_resource_type.serialize_json(
            value["target_resource_type"]
        )
    return out


def deserialize_json(data: dict) -> GetTargetResourceTypeResponse:
    out: GetTargetResourceTypeResponse = {}  # type: ignore[typeddict-item]
    if "targetResourceType" in data:
        import capo_fis.types.target_resource_type

        out["target_resource_type"] = (
            capo_fis.types.target_resource_type.deserialize_json(
                data["targetResourceType"]
            )
        )
    return out
