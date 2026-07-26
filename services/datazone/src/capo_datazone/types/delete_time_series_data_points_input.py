"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteTimeSeriesDataPointsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.entity_identifier
    import capo_datazone.types.time_series_entity_type
    import capo_datazone.types.time_series_form_name


class DeleteTimeSeriesDataPointsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain that houses the asset for which you want to delete a time series form.</p>"""
    entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of the asset for which you want to delete a time series form.</p>"""
    entity_type: "capo_datazone.types.time_series_entity_type.TimeSeriesEntityType"
    """<p>The type of the asset for which you want to delete a time series form.</p>"""
    form_name: "capo_datazone.types.time_series_form_name.TimeSeriesFormName"
    """<p>The name of the time series form that you want to delete.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTimeSeriesDataPointsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTimeSeriesDataPointsInput:
    out: DeleteTimeSeriesDataPointsInput = {}  # type: ignore[typeddict-item]
    return out
