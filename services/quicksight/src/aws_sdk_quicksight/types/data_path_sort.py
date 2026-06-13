"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPathSort``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_path_value_list
    import aws_sdk_quicksight.types.sort_direction


class DataPathSort(TypedDict):
    direction: "aws_sdk_quicksight.types.sort_direction.SortDirection"
    """<p>Determines the sort direction.</p>"""
    sort_paths: "aws_sdk_quicksight.types.data_path_value_list.DataPathValueList"
    """<p>The list of data paths that need to be sorted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPathSort) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.sort_direction

    out["Direction"] = aws_sdk_quicksight.types.sort_direction.serialize_json(
        value["direction"]
    )
    import aws_sdk_quicksight.types.data_path_value_list

    out["SortPaths"] = aws_sdk_quicksight.types.data_path_value_list.serialize_json(
        value["sort_paths"]
    )
    return out


def deserialize_json(data: dict) -> DataPathSort:
    out: DataPathSort = {}  # type: ignore[typeddict-item]
    if "Direction" in data:
        import aws_sdk_quicksight.types.sort_direction

        out["direction"] = aws_sdk_quicksight.types.sort_direction.deserialize_json(
            data["Direction"]
        )
    else:
        raise DeserializationError("DataPathSort.direction required")
    if "SortPaths" in data:
        import aws_sdk_quicksight.types.data_path_value_list

        out["sort_paths"] = (
            aws_sdk_quicksight.types.data_path_value_list.deserialize_json(
                data["SortPaths"]
            )
        )
    else:
        raise DeserializationError("DataPathSort.sort_paths required")
    return out
