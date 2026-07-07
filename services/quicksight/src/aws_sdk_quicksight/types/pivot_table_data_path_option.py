"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableDataPathOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_path_value_list
    import aws_sdk_quicksight.types.pixel_length


class PivotTableDataPathOption(TypedDict, closed=True):
    data_path_list: "aws_sdk_quicksight.types.data_path_value_list.DataPathValueList"
    """<p>The list of data path values for the data path options.</p>"""
    width: NotRequired["aws_sdk_quicksight.types.pixel_length.PixelLength"]
    """<p>The width of the data path option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableDataPathOption) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.data_path_value_list

    out["DataPathList"] = aws_sdk_quicksight.types.data_path_value_list.serialize_json(
        value["data_path_list"]
    )
    if "width" in value:
        out["Width"] = value["width"]
    return out


def deserialize_json(data: dict) -> PivotTableDataPathOption:
    out: PivotTableDataPathOption = {}  # type: ignore[typeddict-item]
    if "DataPathList" in data:
        import aws_sdk_quicksight.types.data_path_value_list

        out["data_path_list"] = (
            aws_sdk_quicksight.types.data_path_value_list.deserialize_json(
                data["DataPathList"]
            )
        )
    else:
        raise DeserializationError("PivotTableDataPathOption.data_path_list required")
    if "Width" in data:
        out["width"] = data["Width"]
    return out
