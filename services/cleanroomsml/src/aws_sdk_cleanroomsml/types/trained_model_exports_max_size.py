"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportsMaxSize``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.trained_model_exports_max_size_unit_type
    import aws_sdk_cleanroomsml.types.trained_model_exports_max_size_value


class TrainedModelExportsMaxSize(TypedDict):
    unit: "aws_sdk_cleanroomsml.types.trained_model_exports_max_size_unit_type.TrainedModelExportsMaxSizeUnitType"
    """<p>The unit of measurement for the data size.</p>"""
    value: "aws_sdk_cleanroomsml.types.trained_model_exports_max_size_value.TrainedModelExportsMaxSizeValue"
    """<p>The maximum size of the dataset to export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelExportsMaxSize) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.trained_model_exports_max_size_unit_type

    out["unit"] = (
        aws_sdk_cleanroomsml.types.trained_model_exports_max_size_unit_type.serialize_json(
            value["unit"]
        )
    )
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TrainedModelExportsMaxSize:
    out: TrainedModelExportsMaxSize = {}  # type: ignore[typeddict-item]
    if "unit" in data:
        import aws_sdk_cleanroomsml.types.trained_model_exports_max_size_unit_type

        out["unit"] = (
            aws_sdk_cleanroomsml.types.trained_model_exports_max_size_unit_type.deserialize_json(
                data["unit"]
            )
        )
    else:
        raise DeserializationError("TrainedModelExportsMaxSize.unit required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("TrainedModelExportsMaxSize.value required")
    return out
