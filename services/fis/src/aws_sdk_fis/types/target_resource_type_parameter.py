"""Generated from Smithy shape ``com.amazonaws.fis#TargetResourceTypeParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.target_resource_type_parameter_description
    import aws_sdk_fis.types.target_resource_type_parameter_required


class TargetResourceTypeParameter(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_fis.types.target_resource_type_parameter_description.TargetResourceTypeParameterDescription"
    ]
    """<p>A description of the parameter.</p>"""
    required: NotRequired[
        "aws_sdk_fis.types.target_resource_type_parameter_required.TargetResourceTypeParameterRequired"
    ]
    """<p>Indicates whether the parameter is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetResourceTypeParameter) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "required" in value:
        out["required"] = value["required"]
    return out


def deserialize_json(data: dict) -> TargetResourceTypeParameter:
    out: TargetResourceTypeParameter = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "required" in data:
        out["required"] = data["required"]
    return out
