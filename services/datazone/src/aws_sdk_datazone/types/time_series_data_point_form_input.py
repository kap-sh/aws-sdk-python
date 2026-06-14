"""Generated from Smithy shape ``com.amazonaws.datazone#TimeSeriesDataPointFormInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.form_type_identifier
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.time_series_form_name


class TimeSeriesDataPointFormInput(TypedDict):
    form_name: "aws_sdk_datazone.types.time_series_form_name.TimeSeriesFormName"
    """<p>The name of the time series data points form.</p>"""
    type_identifier: "aws_sdk_datazone.types.form_type_identifier.FormTypeIdentifier"
    """<p>The ID of the type of the time series data points form.</p>"""
    type_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision type of the time series data points form.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp of the time series data points form.</p>"""
    content: NotRequired["str"]
    """<p>The content of the time series data points form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesDataPointFormInput) -> dict:
    out: dict = {}
    out["formName"] = value["form_name"]
    out["typeIdentifier"] = value["type_identifier"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    import aws_sdk_datazone.types._prelude.timestamp

    out["timestamp"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "content" in value:
        out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> TimeSeriesDataPointFormInput:
    out: TimeSeriesDataPointFormInput = {}  # type: ignore[typeddict-item]
    if "formName" in data:
        out["form_name"] = data["formName"]
    else:
        raise DeserializationError("TimeSeriesDataPointFormInput.form_name required")
    if "typeIdentifier" in data:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        raise DeserializationError(
            "TimeSeriesDataPointFormInput.type_identifier required"
        )
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    if "timestamp" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["timestamp"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("TimeSeriesDataPointFormInput.timestamp required")
    if "content" in data:
        out["content"] = data["content"]
    return out
