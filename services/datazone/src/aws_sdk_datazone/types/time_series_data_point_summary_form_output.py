"""Generated from Smithy shape ``com.amazonaws.datazone#TimeSeriesDataPointSummaryFormOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.data_point_identifier
    import aws_sdk_datazone.types.form_type_identifier
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.time_series_form_name


class TimeSeriesDataPointSummaryFormOutput(TypedDict, closed=True):
    form_name: "aws_sdk_datazone.types.time_series_form_name.TimeSeriesFormName"
    """<p>The name of the time series data points summary form.</p>"""
    type_identifier: "aws_sdk_datazone.types.form_type_identifier.FormTypeIdentifier"
    """<p>The type ID of the time series data points summary form.</p>"""
    type_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The type revision of the time series data points summary form.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp of the time series data points summary form.</p>"""
    content_summary: NotRequired["str"]
    """<p>The content of the summary of the time series data points form.</p>"""
    id: NotRequired["aws_sdk_datazone.types.data_point_identifier.DataPointIdentifier"]
    """<p>The ID of the time series data points summary form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesDataPointSummaryFormOutput) -> dict:
    out: dict = {}
    out["formName"] = value["form_name"]
    out["typeIdentifier"] = value["type_identifier"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    import aws_sdk_datazone.types._prelude.timestamp

    out["timestamp"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "content_summary" in value:
        out["contentSummary"] = value["content_summary"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> TimeSeriesDataPointSummaryFormOutput:
    out: TimeSeriesDataPointSummaryFormOutput = {}  # type: ignore[typeddict-item]
    if "formName" in data:
        out["form_name"] = data["formName"]
    else:
        raise DeserializationError(
            "TimeSeriesDataPointSummaryFormOutput.form_name required"
        )
    if "typeIdentifier" in data:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        raise DeserializationError(
            "TimeSeriesDataPointSummaryFormOutput.type_identifier required"
        )
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    if "timestamp" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["timestamp"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError(
            "TimeSeriesDataPointSummaryFormOutput.timestamp required"
        )
    if "contentSummary" in data:
        out["content_summary"] = data["contentSummary"]
    if "id" in data:
        out["id"] = data["id"]
    return out
