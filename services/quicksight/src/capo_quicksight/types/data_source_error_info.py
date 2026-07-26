"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceErrorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_source_error_info_type
    import capo_quicksight.types.string


class DataSourceErrorInfo(TypedDict, closed=True):
    type: NotRequired[
        "capo_quicksight.types.data_source_error_info_type.DataSourceErrorInfoType"
    ]
    """<p>Error type.</p>"""
    message: NotRequired["capo_quicksight.types.string.String"]
    """<p>Error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceErrorInfo) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_quicksight.types.data_source_error_info_type

        out["Type"] = capo_quicksight.types.data_source_error_info_type.serialize_json(
            value["type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DataSourceErrorInfo:
    out: DataSourceErrorInfo = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_quicksight.types.data_source_error_info_type

        out["type"] = (
            capo_quicksight.types.data_source_error_info_type.deserialize_json(
                data["Type"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
