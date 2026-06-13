"""Generated from Smithy shape ``com.amazonaws.datazone#GetTimeSeriesDataPointInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.entity_identifier
    import aws_sdk_datazone.types.time_series_data_point_identifier
    import aws_sdk_datazone.types.time_series_entity_type
    import aws_sdk_datazone.types.time_series_form_name


class GetTimeSeriesDataPointInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain that houses the asset for which you want to get the data point.</p>"""
    entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of the asset for which you want to get the data point.</p>"""
    entity_type: "aws_sdk_datazone.types.time_series_entity_type.TimeSeriesEntityType"
    """<p>The type of the asset for which you want to get the data point.</p>"""
    identifier: "aws_sdk_datazone.types.time_series_data_point_identifier.TimeSeriesDataPointIdentifier"
    """<p>The ID of the data point that you want to get.</p>"""
    form_name: "aws_sdk_datazone.types.time_series_form_name.TimeSeriesFormName"
    """<p>The name of the time series form that houses the data point that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTimeSeriesDataPointInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTimeSeriesDataPointInput:
    out: GetTimeSeriesDataPointInput = {}  # type: ignore[typeddict-item]
    return out
