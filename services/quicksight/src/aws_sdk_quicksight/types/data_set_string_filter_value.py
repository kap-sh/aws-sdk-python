"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringFilterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_string_filter_static_value


class DataSetStringFilterValue(TypedDict, closed=True):
    static_value: NotRequired[
        "aws_sdk_quicksight.types.data_set_string_filter_static_value.DataSetStringFilterStaticValue"
    ]
    """<p>A static string value used for filtering.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStringFilterValue) -> dict:
    out: dict = {}
    if "static_value" in value:
        out["StaticValue"] = value["static_value"]
    return out


def deserialize_json(data: dict) -> DataSetStringFilterValue:
    out: DataSetStringFilterValue = {}  # type: ignore[typeddict-item]
    if "StaticValue" in data:
        out["static_value"] = data["StaticValue"]
    return out
