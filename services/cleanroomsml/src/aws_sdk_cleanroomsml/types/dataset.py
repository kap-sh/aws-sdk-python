"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#Dataset``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.dataset_input_config
    import aws_sdk_cleanroomsml.types.dataset_type


class Dataset(TypedDict):
    type: "aws_sdk_cleanroomsml.types.dataset_type.DatasetType"
    """<p>What type of information is found in the dataset.</p>"""
    input_config: "aws_sdk_cleanroomsml.types.dataset_input_config.DatasetInputConfig"
    """<p>A DatasetInputConfig object that defines the data source and schema mapping.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dataset) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.dataset_type

    out["type"] = aws_sdk_cleanroomsml.types.dataset_type.serialize_json(value["type"])
    import aws_sdk_cleanroomsml.types.dataset_input_config

    out["inputConfig"] = aws_sdk_cleanroomsml.types.dataset_input_config.serialize_json(
        value["input_config"]
    )
    return out


def deserialize_json(data: dict) -> Dataset:
    out: Dataset = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_cleanroomsml.types.dataset_type

        out["type"] = aws_sdk_cleanroomsml.types.dataset_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("Dataset.type required")
    if "inputConfig" in data:
        import aws_sdk_cleanroomsml.types.dataset_input_config

        out["input_config"] = (
            aws_sdk_cleanroomsml.types.dataset_input_config.deserialize_json(
                data["inputConfig"]
            )
        )
    else:
        raise DeserializationError("Dataset.input_config required")
    return out
