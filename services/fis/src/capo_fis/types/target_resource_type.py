"""Generated from Smithy shape ``com.amazonaws.fis#TargetResourceType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.target_resource_type_description
    import capo_fis.types.target_resource_type_id
    import capo_fis.types.target_resource_type_parameter_map


class TargetResourceType(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_fis.types.target_resource_type_id.TargetResourceTypeId"
    ]
    """<p>The resource type.</p>"""
    description: NotRequired[
        "capo_fis.types.target_resource_type_description.TargetResourceTypeDescription"
    ]
    """<p>A description of the resource type.</p>"""
    parameters: NotRequired[
        "capo_fis.types.target_resource_type_parameter_map.TargetResourceTypeParameterMap"
    ]
    """<p>The parameters for the resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetResourceType) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "description" in value:
        out["description"] = value["description"]
    if "parameters" in value:
        import capo_fis.types.target_resource_type_parameter_map

        out["parameters"] = (
            capo_fis.types.target_resource_type_parameter_map.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> TargetResourceType:
    out: TargetResourceType = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "description" in data:
        out["description"] = data["description"]
    if "parameters" in data:
        import capo_fis.types.target_resource_type_parameter_map

        out["parameters"] = (
            capo_fis.types.target_resource_type_parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    return out
