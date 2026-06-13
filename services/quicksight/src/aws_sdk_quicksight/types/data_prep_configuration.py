"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPrepConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.destination_table_map
    import aws_sdk_quicksight.types.source_table_map
    import aws_sdk_quicksight.types.transform_step_map


class DataPrepConfiguration(TypedDict):
    source_table_map: "aws_sdk_quicksight.types.source_table_map.SourceTableMap"
    """<p>A map of source tables that provide information about underlying sources.</p>"""
    transform_step_map: "aws_sdk_quicksight.types.transform_step_map.TransformStepMap"
    """<p>A map of transformation steps that process the data.</p>"""
    destination_table_map: (
        "aws_sdk_quicksight.types.destination_table_map.DestinationTableMap"
    )
    """<p>A map of destination tables that receive the final prepared data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPrepConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.source_table_map

    out["SourceTableMap"] = aws_sdk_quicksight.types.source_table_map.serialize_json(
        value["source_table_map"]
    )
    import aws_sdk_quicksight.types.transform_step_map

    out["TransformStepMap"] = (
        aws_sdk_quicksight.types.transform_step_map.serialize_json(
            value["transform_step_map"]
        )
    )
    import aws_sdk_quicksight.types.destination_table_map

    out["DestinationTableMap"] = (
        aws_sdk_quicksight.types.destination_table_map.serialize_json(
            value["destination_table_map"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataPrepConfiguration:
    out: DataPrepConfiguration = {}  # type: ignore[typeddict-item]
    if "SourceTableMap" in data:
        import aws_sdk_quicksight.types.source_table_map

        out["source_table_map"] = (
            aws_sdk_quicksight.types.source_table_map.deserialize_json(
                data["SourceTableMap"]
            )
        )
    else:
        raise DeserializationError("DataPrepConfiguration.source_table_map required")
    if "TransformStepMap" in data:
        import aws_sdk_quicksight.types.transform_step_map

        out["transform_step_map"] = (
            aws_sdk_quicksight.types.transform_step_map.deserialize_json(
                data["TransformStepMap"]
            )
        )
    else:
        raise DeserializationError("DataPrepConfiguration.transform_step_map required")
    if "DestinationTableMap" in data:
        import aws_sdk_quicksight.types.destination_table_map

        out["destination_table_map"] = (
            aws_sdk_quicksight.types.destination_table_map.deserialize_json(
                data["DestinationTableMap"]
            )
        )
    else:
        raise DeserializationError(
            "DataPrepConfiguration.destination_table_map required"
        )
    return out
