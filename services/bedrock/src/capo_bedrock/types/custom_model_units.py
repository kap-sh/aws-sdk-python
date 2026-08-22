"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomModelUnits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.custom_model_units_version


class CustomModelUnits(TypedDict, closed=True):
    custom_model_units_per_model_copy: NotRequired["int"]
    """<p>The number of custom model units used to host a model copy. </p>"""
    custom_model_units_version: NotRequired[
        "capo_bedrock.types.custom_model_units_version.CustomModelUnitsVersion"
    ]
    """<p>The version of the custom model unit. Use to determine the billing rate for the custom model unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomModelUnits) -> dict:
    out: dict = {}
    if "custom_model_units_per_model_copy" in value:
        out["customModelUnitsPerModelCopy"] = value["custom_model_units_per_model_copy"]
    if "custom_model_units_version" in value:
        out["customModelUnitsVersion"] = value["custom_model_units_version"]
    return out


def deserialize_json(data: dict) -> CustomModelUnits:
    out: CustomModelUnits = {}  # type: ignore[typeddict-item]
    if data.get("customModelUnitsPerModelCopy") is not None:
        out["custom_model_units_per_model_copy"] = data["customModelUnitsPerModelCopy"]
    if data.get("customModelUnitsVersion") is not None:
        out["custom_model_units_version"] = data["customModelUnitsVersion"]
    return out
