"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelArtifactMaxSize``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_artifact_max_size_unit_type
    import capo_cleanroomsml.types.trained_model_artifact_max_size_value


class TrainedModelArtifactMaxSize(TypedDict, closed=True):
    unit: "capo_cleanroomsml.types.trained_model_artifact_max_size_unit_type.TrainedModelArtifactMaxSizeUnitType"
    """<p>The unit of measurement for the maximum artifact size. Valid values include common storage units such as bytes, kilobytes, megabytes, gigabytes, and terabytes.</p>"""
    value: "capo_cleanroomsml.types.trained_model_artifact_max_size_value.TrainedModelArtifactMaxSizeValue"
    """<p>The numerical value for the maximum artifact size limit. This value is interpreted according to the specified unit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelArtifactMaxSize) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.trained_model_artifact_max_size_unit_type

    out["unit"] = (
        capo_cleanroomsml.types.trained_model_artifact_max_size_unit_type.serialize_json(
            value["unit"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TrainedModelArtifactMaxSize:
    out: TrainedModelArtifactMaxSize = {}  # type: ignore[typeddict-item]
    if "unit" in data:
        import capo_cleanroomsml.types.trained_model_artifact_max_size_unit_type

        out["unit"] = (
            capo_cleanroomsml.types.trained_model_artifact_max_size_unit_type.deserialize_json(
                data["unit"]
            )
        )
    else:
        raise DeserializationError("TrainedModelArtifactMaxSize.unit required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("TrainedModelArtifactMaxSize.value required")
    return out
