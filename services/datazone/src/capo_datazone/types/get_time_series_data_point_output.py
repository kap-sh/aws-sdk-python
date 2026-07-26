"""Generated from Smithy shape ``com.amazonaws.datazone#GetTimeSeriesDataPointOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.entity_id
    import capo_datazone.types.time_series_data_point_form_output
    import capo_datazone.types.time_series_entity_type
    import capo_datazone.types.time_series_form_name


class GetTimeSeriesDataPointOutput(TypedDict, closed=True):
    domain_id: NotRequired["capo_datazone.types.domain_id.DomainId"]
    """<p>The ID of the Amazon DataZone domain that houses the asset data point that you want to get.</p>"""
    entity_id: NotRequired["capo_datazone.types.entity_id.EntityId"]
    """<p>The ID of the asset for which you want to get the data point.</p>"""
    entity_type: NotRequired[
        "capo_datazone.types.time_series_entity_type.TimeSeriesEntityType"
    ]
    """<p>The type of the asset for which you want to get the data point.</p>"""
    form_name: NotRequired[
        "capo_datazone.types.time_series_form_name.TimeSeriesFormName"
    ]
    """<p>The name of the time series form that houses the data point that you want to get.</p>"""
    form: NotRequired[
        "capo_datazone.types.time_series_data_point_form_output.TimeSeriesDataPointFormOutput"
    ]
    """<p>The time series form that houses the data point that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTimeSeriesDataPointOutput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "entity_type" in value:
        import capo_datazone.types.time_series_entity_type

        out["entityType"] = capo_datazone.types.time_series_entity_type.serialize_json(
            value["entity_type"]
        )
    if "form_name" in value:
        out["formName"] = value["form_name"]
    if "form" in value:
        import capo_datazone.types.time_series_data_point_form_output

        out["form"] = (
            capo_datazone.types.time_series_data_point_form_output.serialize_json(
                value["form"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTimeSeriesDataPointOutput:
    out: GetTimeSeriesDataPointOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "entityType" in data:
        import capo_datazone.types.time_series_entity_type

        out["entity_type"] = (
            capo_datazone.types.time_series_entity_type.deserialize_json(
                data["entityType"]
            )
        )
    if "formName" in data:
        out["form_name"] = data["formName"]
    if "form" in data:
        import capo_datazone.types.time_series_data_point_form_output

        out["form"] = (
            capo_datazone.types.time_series_data_point_form_output.deserialize_json(
                data["form"]
            )
        )
    return out
