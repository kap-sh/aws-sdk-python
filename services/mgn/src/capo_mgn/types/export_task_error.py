"""Generated from Smithy shape ``com.amazonaws.mgn#ExportTaskError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.export_error_data
    import capo_mgn.types.iso8601_datetime_string


class ExportTaskError(TypedDict, closed=True):
    error_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Export task error datetime.</p>"""
    error_data: NotRequired["capo_mgn.types.export_error_data.ExportErrorData"]
    """<p>Export task error data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportTaskError) -> dict:
    out: dict = {}
    if "error_date_time" in value:
        out["errorDateTime"] = value["error_date_time"]
    if "error_data" in value:
        import capo_mgn.types.export_error_data

        out["errorData"] = capo_mgn.types.export_error_data.serialize_json(
            value["error_data"]
        )
    return out


def deserialize_json(data: dict) -> ExportTaskError:
    out: ExportTaskError = {}  # type: ignore[typeddict-item]
    if "errorDateTime" in data:
        out["error_date_time"] = data["errorDateTime"]
    if "errorData" in data:
        import capo_mgn.types.export_error_data

        out["error_data"] = capo_mgn.types.export_error_data.deserialize_json(
            data["errorData"]
        )
    return out
