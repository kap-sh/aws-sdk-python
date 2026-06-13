"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filled_map_aggregated_field_wells


class FilledMapFieldWells(TypedDict):
    filled_map_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.filled_map_aggregated_field_wells.FilledMapAggregatedFieldWells"
    ]
    """<p>The aggregated field well of the filled map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapFieldWells) -> dict:
    out: dict = {}
    if "filled_map_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.filled_map_aggregated_field_wells

        out["FilledMapAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.filled_map_aggregated_field_wells.serialize_json(
                value["filled_map_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilledMapFieldWells:
    out: FilledMapFieldWells = {}  # type: ignore[typeddict-item]
    if "FilledMapAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.filled_map_aggregated_field_wells

        out["filled_map_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.filled_map_aggregated_field_wells.deserialize_json(
                data["FilledMapAggregatedFieldWells"]
            )
        )
    return out
