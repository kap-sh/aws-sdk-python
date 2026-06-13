"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteTimeSeriesDataPointsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.client_token
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.entity_identifier
    import aws_sdk_datazone.types.time_series_entity_type
    import aws_sdk_datazone.types.time_series_form_name


class DeleteTimeSeriesDataPointsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain that houses the asset for which you want to delete a time series form.</p>"""
    entity_identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of the asset for which you want to delete a time series form.</p>"""
    entity_type: "aws_sdk_datazone.types.time_series_entity_type.TimeSeriesEntityType"
    """<p>The type of the asset for which you want to delete a time series form.</p>"""
    form_name: "aws_sdk_datazone.types.time_series_form_name.TimeSeriesFormName"
    """<p>The name of the time series form that you want to delete.</p>"""
    client_token: NotRequired["aws_sdk_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTimeSeriesDataPointsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTimeSeriesDataPointsInput:
    out: DeleteTimeSeriesDataPointsInput = {}  # type: ignore[typeddict-item]
    return out
