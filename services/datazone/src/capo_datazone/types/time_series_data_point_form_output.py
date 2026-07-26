"""Generated from Smithy shape ``com.amazonaws.datazone#TimeSeriesDataPointFormOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.data_point_identifier
    import capo_datazone.types.form_type_identifier
    import capo_datazone.types.revision
    import capo_datazone.types.time_series_form_name


class TimeSeriesDataPointFormOutput(TypedDict, closed=True):
    form_name: "capo_datazone.types.time_series_form_name.TimeSeriesFormName"
    """<p>The name of the time series data points form.</p>"""
    type_identifier: "capo_datazone.types.form_type_identifier.FormTypeIdentifier"
    """<p>The ID of the type of the time series data points form.</p>"""
    type_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision type of the time series data points form.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp of the time series data points form.</p>"""
    content: NotRequired["str"]
    """<p>The content of the time series data points form.</p>"""
    id: NotRequired["capo_datazone.types.data_point_identifier.DataPointIdentifier"]
    """<p>The ID of the time series data points form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesDataPointFormOutput) -> dict:
    out: dict = {}
    out["formName"] = value["form_name"]
    out["typeIdentifier"] = value["type_identifier"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    import capo_datazone.types._prelude.timestamp

    out["timestamp"] = capo_datazone.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "content" in value:
        out["content"] = value["content"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> TimeSeriesDataPointFormOutput:
    out: TimeSeriesDataPointFormOutput = {}  # type: ignore[typeddict-item]
    if "formName" in data:
        out["form_name"] = data["formName"]
    else:
        raise DeserializationError("TimeSeriesDataPointFormOutput.form_name required")
    if "typeIdentifier" in data:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        raise DeserializationError(
            "TimeSeriesDataPointFormOutput.type_identifier required"
        )
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    if "timestamp" in data:
        import capo_datazone.types._prelude.timestamp

        out["timestamp"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("TimeSeriesDataPointFormOutput.timestamp required")
    if "content" in data:
        out["content"] = data["content"]
    if "id" in data:
        out["id"] = data["id"]
    return out
