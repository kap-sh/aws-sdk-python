"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelInferenceMaxOutputSize``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type
    import capo_cleanroomsml.types.trained_model_inference_max_output_size_value


class TrainedModelInferenceMaxOutputSize(TypedDict, closed=True):
    unit: "capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type.TrainedModelInferenceMaxOutputSizeUnitType"
    """<p>The measurement unit to use.</p>"""
    value: "capo_cleanroomsml.types.trained_model_inference_max_output_size_value.TrainedModelInferenceMaxOutputSizeValue"
    """<p>The maximum output size value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelInferenceMaxOutputSize) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type

    out["unit"] = (
        capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type.serialize_json(
            value["unit"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TrainedModelInferenceMaxOutputSize:
    out: TrainedModelInferenceMaxOutputSize = {}  # type: ignore[typeddict-item]
    if "unit" in data:
        import capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type

        out["unit"] = (
            capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type.deserialize_json(
                data["unit"]
            )
        )
    else:
        raise DeserializationError("TrainedModelInferenceMaxOutputSize.unit required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("TrainedModelInferenceMaxOutputSize.value required")
    return out
